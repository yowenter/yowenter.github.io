from sphinx.builders.html import StandaloneHTMLBuilder


class OptimizedHTMLBuilder(StandaloneHTMLBuilder):
    name = 'Ohtml'
    script_files = []



def setup(app):
    app.add_builder(OptimizedHTMLBuilder)
