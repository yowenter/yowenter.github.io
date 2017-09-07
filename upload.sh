rm -rf dist
rm -rf taoge_blog.egg-info
source venv/bin/activate
python setup.py sdist
twine upload dist/*
