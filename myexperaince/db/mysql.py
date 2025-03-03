def insertdb(query, values):
    print(f"INSERT QUERY: {query.format(*values)}")


def update(query, values):
    print(f"UPDATE QUERY: {query.format(*values)}")


def delete(query, values):
    print(f"DELETE QUERY: {query.format(*values)}")


def select(query, values=None):
    print(f"SELECT QUERY: {query.format(*(values or ())) }")


insertdb("INSERT INTO users (name, age) VALUES ('{}', {})", ("Ali", 25))
update("UPDATE users SET age = {} WHERE name = '{}'", (26, "Ali"))
delete("DELETE FROM users WHERE name = '{}'", ("Ali",))
select("SELECT * FROM users WHERE age > {}", (20,))
