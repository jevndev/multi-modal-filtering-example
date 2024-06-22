install:
	python3.12 -m venv ./.venv
	./.venv/bin/pip install --upgrade pip
	./.venv/bin/pip install	uv==0.2.13
	./.venv/bin/python -m uv pip install -r requirements.txt
	./.venv/bin/python -m uv pip install -e .

test:
	./.venv/bin/pytest tests

run:
	./.venv/bin/python -m multi_modal_filtering_example

clean:
	rm -rf ./.venv
	rm -rf ./.pytest_cache
	rm -rf ./**/__pycache__
	rm -rf ./**/*.egg-info
