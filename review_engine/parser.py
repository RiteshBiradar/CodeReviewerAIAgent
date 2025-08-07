from tree_sitter import Language, Parser
import os

# Load the pre-built grammar
LIB_PATH = os.path.join(os.path.dirname(__file__), '..', 'build', 'my-languages.so')

PY_LANGUAGE = Language(LIB_PATH, 'python')
JS_LANGUAGE = Language(LIB_PATH, 'javascript')

class CodeParser:
    def __init__(self, language: str):
        self.parser = Parser()
        if language == "python":
            self.parser.set_language(PY_LANGUAGE)
        elif language == "javascript":
            self.parser.set_language(JS_LANGUAGE)
        else:
            raise ValueError("Unsupported language")

    def parse_code(self, code: str):
        tree = self.parser.parse(code.encode())
        return self.extract_structure(tree.root_node, code.encode())

    def extract_structure(self, node, code, parent_function=None, results=None):
        if results is None:
            results = []

        if node.type in ["function_definition", "function_declaration"]:
            name_node = node.child_by_field_name("name")
            name = code[name_node.start_byte:name_node.end_byte].decode()
            results.append({
                "type": "function",
                "name": name,
                "start_line": node.start_point[0] + 1,
                "end_line": node.end_point[0] + 1,
                "parent": parent_function,
            })
            parent_function = name  # update parent

        if node.type == "import_statement" or node.type == "import_from_statement":
            results.append({
                "type": "import",
                "text": code[node.start_byte:node.end_byte].decode(),
                "line": node.start_point[0] + 1,
            })

        for child in node.children:
            self.extract_structure(child, code, parent_function, results)

        return results
