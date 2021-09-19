from os import name
from flask_restful import Resource, reqparse
import mariadb


class Items(Resource):

    my_parser = reqparse.RequestParser()
    my_parser.add_argument(
        "name",
        type=str,
        required=True,
        help="The name field cannot be blank"
    )
    my_parser.add_argument(
        "price",
        type=str,
        required=True,
        help="The price field cannot be blank"
    )

    @staticmethod
    def find_by_name(item_name):
        my_db_connection = mariadb.connect(
            user="jsmith",
            password="J@ckson4",
            host="192.168.127.142",
            database="mydb"
        )
        my_db_cursor = my_db_connection.cursor()
        sql_command = "SELECT * FROM items WHERE name = ?"
        my_db_cursor.execute(sql_command, (item_name,))
        final_result = my_db_cursor.fetchone()
        my_db_connection.close()
        if final_result:
            return {"name": final_result[1], "price": final_result[2]}
        else:
            return None

    def get(self):
        incoming_data = Items.my_parser.parse_args()
        item_in_db = Items.find_by_name(incoming_data["name"])
        if item_in_db:
            return {"status": "success", "data": item_in_db}, 200
        else:
            return {"status": "fail", "message": "item not available"}, 404
