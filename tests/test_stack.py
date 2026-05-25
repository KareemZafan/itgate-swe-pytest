
import pytest 
from src.stack import Stack


def test_push():
    st = Stack()
    assert st.is_empty() == True
    
    st.push(1)
    st.push(2)
    st.push(1000)
    st.push(-9000)
    assert st.get_stack_size() == 4
    assert st.get_peek() == -9000
    assert st.is_empty() == False
    assert st.get_stack_items() == [1,2,1000,-9000]

    ## Value to be popped is -9000
    value = st.pop()
    assert value == -9000
    assert st.get_stack_items() == [1,2,1000]
    assert st.get_stack_size() == 3
    assert st.get_peek() == 1000

    st.clear_stack()
    assert st.is_empty() == True
    assert st.get_stack_items() == []
    assert st.get_stack_size() == 0 





def test_pop():
    st = Stack()
    assert st.is_empty() == True
    
    st.push(1)
    st.push(2)
    st.push(1000)
    st.push(-9000)
    st.push(60000)
    assert st.get_stack_size() == 5
    assert st.get_peek() == 60000
    assert st.is_empty() == False
    assert st.get_stack_items() == [1,2,1000,-9000,60000]   

    ls = []
    ls.append(st.pop())
    ls.append(st.pop())
    ls.append(st.pop())

    assert ls == [60000,-9000,1000]
    assert st.get_peek() == 2
    assert st.get_stack_size() == 2
    assert st.get_stack_items() == [1,2]
    assert st.is_empty() == False

    st.clear_stack()
    assert st.is_empty() == True
    assert st.get_stack_items() == []
    assert st.get_stack_size() == 0 

    






