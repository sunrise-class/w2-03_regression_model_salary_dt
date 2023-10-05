import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="flask_db",
    host="localhost",
    port=5433,
    user="postgres",
    password="asdfa"
)

try:
    # Create a cursor object
    cursor = conn.cursor()

    # Execute the INSERT statement with a RETURNING clause to retrieve data
    cursor.execute("""
    INSERT INTO book (book_name)
    VALUES (%s)
    RETURNING id, book_name;
    """,
    ("Fiction",))

    # Fetch the result row
    book = cursor.fetchone()

    if book:
        book_id, book_name = book
        print(f"Record inserted successfully with ID {book_id}: {book_name}")
    else:
        print("No records returned.")

    # Commit the transaction
    conn.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while inserting into PostgreSQL:", error)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()