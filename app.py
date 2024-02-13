import json
from flask import Flask, g, jsonify, request
from database import get_db
from functools import wraps

app = Flask(__name__)

api_username = "admin"
api_password = "pass"


def protected(foo):
    @wraps(foo)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == api_username and auth.password == api_password:
            return foo(*args, **kwargs)
        return jsonify({"message": "Authentication failed!"}), 403

    return decorated


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()


@app.route("/member", methods=["GET"])
@protected
def get_members():
    db = get_db()

    members_cur = db.execute("SELECT id, name, email, level FROM members")
    members = members_cur.fetchall()

    return_values = []
    for member in members:
        member_dict = {}
        member_dict["id"] = member["id"]
        member_dict["name"] = member["name"]
        member_dict["email"] = member["email"]
        member_dict["level"] = member["level"]

        return_values.append(member_dict)

    return jsonify({"members": return_values})


@app.route("/member/<int:member_id>", methods=["GET"])
@protected
def get_member(member_id):
    db = get_db()
    member_cur = db.execute(
        "SELECT id, name, email, level FROM members WHERE id = ?", [member_id]
    )
    member = member_cur.fetchone()
    return jsonify(
        {
            "member": {
                "id": member["id"],
                "name": member["name"],
                "email": member["email"],
                "level": member["level"],
            }
        }
    )


@app.route("/member", methods=["POST"])
@protected
def add_member():
    new_member_data = request.get_json()

    name = new_member_data["name"]
    email = new_member_data["email"]
    level = new_member_data["level"]

    db = get_db()
    db.execute(
        "INSERT INTO members (name, email, level) VALUES (?, ?, ?)",
        [name, email, level],
    )
    db.commit()

    member_cur = db.execute(
        "SELECT id, name, level FROM members WHERE name = ?", [name]
    )
    new_member = member_cur.fetchone()

    return jsonify(
        {
            "member": {
                "id": new_member["id"],
                "name": new_member["name"],
                "level": new_member["level"],
            }
        }
    )


@app.route("/member/<int:member_id>", methods=["PUT", "PATCH"])
@protected
def edit_member(member_id):
    new_member_data = request.get_json()

    name = new_member_data["name"]
    email = new_member_data["email"]
    level = new_member_data["level"]

    db = get_db()

    db.execute(
        "UPDATE members SET name = ?, email = ?, level = ? WHERE id = ?",
        [name, email, level, member_id],
    )
    db.commit()

    member_cur = db.execute(
        "SELECT id, name, email, level FROM members WHERE id = ?", [member_id]
    )
    member = member_cur.fetchone()

    return jsonify(
        {
            "member": {
                "id": member["id"],
                "name": member["name"],
                "email": member["email"],
                "level": member["level"],
            }
        }
    )


@app.route("/member/<int:member_id>", methods=["DELETE"])
@protected
def delete_member(member_id):
    db = get_db()
    db.execute("DELETE FROM members WHERE id = ?", [member_id])
    db.commit()
    return jsonify({"message": "Member deleted"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
