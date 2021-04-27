from app import app
from sqlConnection import create_connection


database = r"pythonsqlite.db"

@app.route('/ads_count/<int:userId>',methods = ['GET'])
def get_ads_count(userId):
    conn = create_connection(database)
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM user where userId="+str(userId))

    rows = cur.fetchall()
    try:
        return str(rows[0][1])
    except Exception:
        return "Index not valid"
