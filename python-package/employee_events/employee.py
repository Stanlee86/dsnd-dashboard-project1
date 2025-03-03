# Import the QueryBase class 
from employee_events.query_base import QueryBase

# Import dependencies needed for SQL execution from the `sql_execution` module
from employee_events.sql_execution import query

# Define a subclass of QueryBase called Employee
class Employee(QueryBase):

    # Set the class attribute `name` to the string "employee"
    name = "employee"

    # Define a method called `names` that receives no arguments.
    # This method should return a list of tuples from an SQL execution.
    def names(self):
        # Query 3:
        # Select the employee's full name and id for all employees.
        query_str = """
            SELECT full_name, employee_id
            FROM employee
        """
        return self.query(query_str)

    # Define a method called `username` that receives an `id` argument.
    # This method should return a list of tuples from an SQL execution.
    def username(self, id):
        # Query 4:
        # Select the full name of the employee with the specified id.
        query_str = f"""
            SELECT full_name
            FROM employee
            WHERE employee_id = {id}
        """
        return self.query(query_str)

    # This method generates the data needed for the machine learning model.
    # When called, it should execute the SQL query and return a Pandas DataFrame.
    def model_data(self, id):
        query_str = f"""
            SELECT SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
        """
        # Execute the query and return the result as a Pandas DataFrame.
        return self.pandas_query(query_str)
