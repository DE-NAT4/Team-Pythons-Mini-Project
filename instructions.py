
def create_table():
    result = """
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                product_name VARCHAR(20) NOT NULL,
                price DECIMAL(10, 2) NOT NULL
            );
            """
    return result