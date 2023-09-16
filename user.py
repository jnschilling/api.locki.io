# user.py

# from datetime import datetime
from flask import make_response, abort

from config import db
from models import User, people_schema, user_schema

# def get_timestamp():
#     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# USERS = {
#     "erd1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssycr6th": {
#         "bech32": "erd1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssycr6th",
#         "herotag": "alice",
#         "timestamp": get_timestamp(),
#     },
#     "erd1spyavw0956vq68xj8y4tenjpq2wd5a9p2c6j8gsz7ztyrnpxrruqzu66jx": {
#         "bech32": "erd1spyavw0956vq68xj8y4tenjpq2wd5a9p2c6j8gsz7ztyrnpxrruqzu66jx",
#         "herotag": "bob",
#         "timestamp": get_timestamp(),
#     }
# }


def create(wallet):
    # bech32 = wallet.get("bech32")
    # herotag = wallet.get("herotag", "")

    # if bech32 and bech32 not in USERS:
    #     USERS[bech32] = {
    #         "bech32": bech32,
    #         "herotag": herotag,
    #         "timestamp": get_timestamp(),
    #     }
    #     return USERS[bech32], 201
    bech32 = wallet.get("bech32")
    existing_user = User.query.filter(User.bech32 == bech32).one_or_none()

    if existing_user is None:
        new_person = user_schema.load(wallet, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return user_schema.dump(new_person), 201
    else:
        abort(
            406,
            f"User with address {bech32} already exists",
        )


def read_all():
    # return list(USERS.values())
    user = User.query.all()
    return people_schema.dump(user)


def read_one(bech32):
    # print(bech32)
    # if bech32 in USERS:
    #     return USERS[bech32]
    user = User.query.filter(User.bech32 == bech32).one_or_none()

    if user is not None:
        return user_schema.dump(user)
    else:
        abort(
            404, f"Person with address {bech32} not found"
        )
