import pytest

def test_sum():
	assert 1+1==2

def test_divide():
	with pytest.raises(ZeroDivisionError) as e:
		num = 1/0
	assert 'division by zero' in str(e.value)
