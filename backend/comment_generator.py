import ast


class CommentGenerator(ast.NodeVisitor):
    """
    Generates structured comments for functions and classes in Python code.
    """

    def __init__(self):
        self.comments = []

    def visit_FunctionDef(self, node):
        """
        Generates comments for functions.
        """
        func_name = node.name
        params = [arg.arg for arg in node.args.args]

        comment = f"# Function: {func_name}\n"
        comment += f"# Purpose: Explain what {func_name} does.\n"

        if params:
            comment += "# Parameters:\n"
            for param in params:
                comment += f"# - {param}: Describe this parameter\n"
        else:
            comment += "# No parameters\n"

        comment += "# Returns: Describe the return value\n"
        self.comments.append((node.lineno, comment))

        self.generic_visit(node)  # Continue visiting child nodes

    def visit_ClassDef(self, node):
        """
        Generates comments for classes.
        """

        class_name = node.name
        comment = f"# Class: {class_name}\n"
        comment += f"# Purpose: Explain the role of {class_name}\n"
        self.comments.append((node.lineno, comment))

        self.generic_visit(node)

    def generate_comments(self, code):
        """
        Parses Python code and generates comments.
        """
        try:
            tree = ast.parse(code)
            self.visit(tree)
            return self.comments
        except SyntaxError:
            return [(0, "# Error: Invalid Python code provided.")]


def apply_comments(code):
    """
    Inserts generated comments into the provided code.
    """
    generator = CommentGenerator()
    comments = generator.generate_comments(code)

    lines = code.split("\n")
    for lineno, comment in sorted(comments, reverse=True):
        lines.insert(lineno - 1, comment)

    return "\n".join(lines)


if __name__ == "__main__":
    sample_code = """
class AIHelper:
    def __init__(self, model_name):
        self.model_name = model_name

    def analyze_code(self, code):
        return "Analysis result"

def main():
    helper = AIHelper("GPT-4")
    print(helper.analyze_code("def add(a, b): return a + b"))
    """

    commented_code = apply_comments(sample_code)
    print(commented_code)
