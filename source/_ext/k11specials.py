from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

# This is closely based on todo extension from the manual.
# Viewers beware: this is not solid Python code.
# I'm not what one could call a dead parrot operator.

from os.path import getmtime
import re

class k11specialrecentlymodified(nodes.General, nodes.Element):
    def __init__(self, contentArg, limitArg):
        super().__init__()
        self.content = contentArg
        self.limit = limitArg

class K11SpecialRecentlyModifiedDirective(SphinxDirective):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    def run(self):
        return [k11specialrecentlymodified(self.content, self.arguments[0])]

def k11special_get_matcher(content):
    expression = "^("
    for line in content:
        for char in line:
            if char == '*':
                expression = expression + '[^/]*'
            elif char == '%':
                expression = expression + '.*'
            else:
                expression = expression + char
        expression = expression + ")|("
    expression = expression + "/)$"
    return re.compile(expression)

def process_k11specialrecentlymodified_nodes(app, doctree, fromdocname):
    env = app.builder.env
    project = env.project
    if not hasattr(project, 'docnames'):
        project.discover()
    if (project.docnames == None):
        project.discover()
    timed_docnames = [(getmtime(env.doc2path(x)), x) for x in project.docnames]
    revordered_docnames = [b for (a, b) in sorted(timed_docnames)]
    ordered_docnames = [x for x in reversed(revordered_docnames)]
    titlemap = env.titles

    for node in doctree.traverse(k11specialrecentlymodified):

        contentNode = nodes.bullet_list()
        ctr = len(ordered_docnames) if node.limit == None else int(node.limit)
        pattern = k11special_get_matcher(node.content)

        for dn in ordered_docnames:
            if not pattern.fullmatch(dn):
                continue
            bulletNode = nodes.list_item()
            entryNode = nodes.paragraph()
            refNode = nodes.reference('', '')
            ti = titlemap[dn].astext()
            innardNode = nodes.Text(ti, ti)
            refNode['refdocname'] = dn
            refNode['refuri'] = app.builder.get_relative_uri(fromdocname, dn)
            refNode.append(innardNode)
            entryNode.append(refNode)
            bulletNode.append(entryNode)
            contentNode.append(bulletNode)
            ctr -= 1
            if ctr <= 0:
                break

        node.replace_self([contentNode])
        #node.replace_self([])

def setup(app):
    app.add_node(k11specialrecentlymodified)
    app.add_directive('k11specialrecentlymodified', K11SpecialRecentlyModifiedDirective)
    app.connect('doctree-resolved', process_k11specialrecentlymodified_nodes)
    return {
        'version': '0.0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
