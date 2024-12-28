import pymysql
from sqlalchemy.exc import SQLAlchemyError

from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor()

    query = ("select products.product_id, products.name,products.uom_id, products.price_per_unit, uom.uom_name "
             "from products inner join uom on products.uom_id=uom.uom_id")

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:

        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    return response

def insert_new_product (connection,product):
    cursor = connection.cursor()
    query = ("insert into products" 
             "(name, uom_id, price_per_unit)" 
             "values (%s,%s,%s)")
    data = (product ['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_product (connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()


def update_product(connection, name, new_price):
    try:
        # Prepare the SQL query with placeholders
        query = """
            UPDATE products
            SET price_per_unit = %s
            WHERE name = %s
        """

        # Use parameterized query to prevent syntax issues and SQL injection
        with connection.cursor() as cursor:
            cursor.execute(query, (new_price, name))
            connection.commit()

        # Check the number of rows affected
        if cursor.rowcount > 0:
            return f"Product '{name}' updated successfully with new price: {new_price}"
        else:
            return f"No product found with name '{name}'."

    except SQLAlchemyError as e:
        print(f"Error updating product: {e}")
        raise

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    # Define product details
    name = "potato"  # Replace with the actual product name
    new_price = 150  # Replace with the new price
    print(update_product(connection,name, new_price))