import json
import pandas as pd
import pymysql


def process_message(message: str) -> str:
    msg = "You said: " + message
    return msg


def connect_mysql(CRED_PATH):
    """
    Create a global db connector
    """
    global cnx
    with open(CRED_PATH) as f:
        creds = json.load(f)
    cnx = pymysql.connect(host=creds['host'],
                          user=creds['user'],
                          password=creds['password'],
                          port=creds['port'],
                          db=creds['database'])
    return cnx


def return_user(cnx, emp_id):
    q1 = '''
        SELECT name FROM daily_attendance.users WHERE emp_id = %s;
    '''

    # Execute the query with the emp_id parameter
    df1 = pd.read_sql(q1, cnx, params=(emp_id,))
    
    # Check if a name is returned and return it as a string
    if not df1.empty:
        return df1.iloc[0]['name']  # Return the first row's 'name' value
    else:
        return None  # Return None if no matching emp_id is found
