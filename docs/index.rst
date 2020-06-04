sphinx-pydantic
===============

**Autogenerate documentation from pydantic objects in Sphinx**

Introduction
------------

Sphinx-pydantic generates schema documentation from pydantic_ models. For example,


.. code-block:: python

    from pydantic import BaseModel, Field

    class Thing(BaseModel):
        """
        An example of a pydantic object from which we 
        can autogenerate schema documentation.
        """
        name: str = Field(
            ...,
            title='name',
            description='Name of this thing',
        )

.. pydantic:: Thing

    from pydantic import BaseModel, Field


    class Thing(BaseModel):
        """
        An example of a pydantic object from which we 
        can autogenerate schema documentation.
        """
        
        name: str = Field(
            ...,
            title='name',
            description='Name of this thing',
        )

How does it work?
-----------------

**Sphinx-pydantic** is an Sphinx extension that provides a new directive for adding a pydantic objects to your page and leverages sphinx-jsonschema_ to generate schema tables. 


.. _pydantic: https://pydantic-docs.helpmanual.io/
.. _sphinx-jsonschema: https://sphinx-jsonschema.readthedocs.io/en/latest/index.html

Add ``sphinx-pydantic`` to the extensions in your Sphinx ``conf.py`` file.


.. code-block:: python
    
    # conf.py
    ...

    extensions = [
        ...,
        'sphinx-pydantic',
    ]


and you can use the ``pydantic`` directive in your ``.rst`` docs. 

.. code-block:: rst

    some text ...

    .. pydantic:: thing.Thing

    some more text ...

``thing.Thing`` is a class (in the ``thing`` module) that subclasses ``pydantic.BaseModel``.
Sphinx-pydantic imports this class and generates schema using pydantic's sweet API.
By default sphinx is calling the `schema_json` function from pydantic BaseModel.
You can customize the displayed schema by implementing a `schema_rst` function inside your class,
which then will be called instead without any arguments.

Installation
------------

Install sphinx-pydantic with ``pip``:

.. code-block::

    pip install sphinx-pydantic
