# To update docs from root dir:
poetry run sphinx-apidoc -f -o docs .
poetry run sphinx-build -b html docs docs/_build/html ## Same as make html from in the docs dir.
# To view, e.g.:
open -a "Google Chrome" docs/_build/html/index.html

# TODO:
# Could set up docs version number to auto-increment along with the project
# Could set auto-setting of the .. versionadded:: version directive for new docs?
