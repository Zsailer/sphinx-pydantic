from .__version__ import __version__

import importlib
import pydantic

# Depend on JsonSchema
JsonSchema = __import__('sphinx-jsonschema').JsonSchema

class PyDanticSchema(JsonSchema):
    """Wrapper around sphinx-jsonschemas native Directive.
    """
    has_content = True

    def __init__(self, directive, arguments, options, content, lineno, 
        content_offset, block_text, state, state_machine):
        # Parse the first argument, the import statement for pydantic object
        pkg_items = arguments[0].split('.')
        pkg_name = pkg_items[0]
        mod_name = '.'.join(pkg_items[0:-1])
        obj_name = pkg_items[-1]

        # Try importing object
        try:
            mod = importlib.import_module(mod_name)
            obj = getattr(mod, obj_name)
        except ImportError as e:
            raise e

        # Verify type.
        if not issubclass(obj, pydantic.BaseModel):
            raise TypeError(f"{arguments[0]} is not a subclass of pydantic.BaseModel.")

        # Generate a json schema from pydantic
        content = obj.schema_json(indent=2)

        # Need to break content into a list to work with jsonschema.
        content = content.split('\n')

        # Pass the new content to sphinx-jsonschema
        super(PyDanticSchema, self).__init__(directive='jsonschema', arguments=[], options=options, 
            content=content, lineno=lineno, content_offset=content_offset, block_text=block_text, 
            state=state, state_machine= state_machine)


def setup(app):
    # Add pydantic directive to sphinx.
    app.add_directive("pydantic", PyDanticSchema)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }