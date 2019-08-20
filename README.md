# Pydantic Sphinx Extension

Generate Sphinx documentation from PyDantic objects.

## Basic Usages

Install this extension using pip:
```
pip install pydantic_sphinx
```

List the extension in your `conf.py` file.
```python
...

extensions = [
    ...,
    'sphinx_pydantic'
]

```

Add a `pydantic` Sphinx directive to your restructured doc file 
```
Some text...

.. pydantic:: package.MyObject

Some other text...
```

Generate your docs.

## Install
```
pip install pydantic_sphinx
```

## Dependencies

* pydantic
* sphinx-jsonschema