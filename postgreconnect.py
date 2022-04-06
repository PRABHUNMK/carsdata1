import psycopg2

def runquery(sql):
    try:
        #Connect to the heroku postgresql database
        connection=psycopg2.connect(user="yfxpgallicmvhs",
                                password="b42a0e5bddc705436e3b39271057b781cc398451ad2292d785d2311927cfbfa1",
                                host="ec2-52-54-212-232.compute-1.amazonaws.com",
                                database="dc802bu83sg0v6")

        #Create a cursor to perform database operations
        cursor=connection.cursor()

        cursor.execute(sql)

        record = cursor.fetchall()

        #Return the cursor to the calling program
        return(record)
    except:
        print("Error while fetching data")
    finally:
        #Close Cursor and Database Connection
        cursor.close()
        connection.close()
        
