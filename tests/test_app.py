from app import index

def test_index():
	assert index() == "<h1>Hello, World!</h1>"

# export PYTHONPATH=app
# pytest