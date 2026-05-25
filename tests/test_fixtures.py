import pytest


## fixture to open the db connection
@pytest.fixture(scope="module",autouse=True)
def open_db_connection():
    print("\nConnecting to the database...\n")

    
@pytest.fixture(scope="module",autouse=True)
## fixture to close the db connection
def close_db_connection():
    yield
    print("\nClosing the database connection...\n")



### testcases that use the above fixtures

def test_insert_into_db():
    print("\nInserting datat into the database...\n")
    

def test_retrieve_from_db():
    print("\nRetrieving data from the database...\n")

def test_update_in_db():
    print("\nUpdating data in the database...\n")

def test_delete_from_db():
    print("\nDeleting data from the database...\n")

