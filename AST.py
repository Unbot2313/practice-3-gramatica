import ast


def format_node(node):
    if isinstance(node, ast.BinOp):
        return f"({format_node(node.left)} {node.op.__class__.__name__} {format_node(node.right)})"
    elif isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Constant):
        return str(node.value)
    elif isinstance(node, ast.Expr):
        return format_node(node.value)
    return ""

def print_ast(node, indent="", last=True):
    # Usar '└── ' para el último nodo y '├── ' para los nodos intermedios
    connector = "└── " if last else "├── "
    print(f"{indent}{connector}{node.op.__class__.__name__ if isinstance(node, ast.BinOp) else ''}")

    if isinstance(node, ast.BinOp):
        # Para los nodos BinOp, imprimir el lado izquierdo y derecho
        print_ast(node.left, indent + ("    " if last else "│   "), False)
        print_ast(node.right, indent + ("    " if last else "│   "), True)
    elif isinstance(node, ast.Expr):
        print_ast(node.value, indent, last)
    elif isinstance(node, ast.Name):
        print(f"{indent}    || {node.id}")  # Añadir tabulación adicional
    elif isinstance(node, ast.Constant):
        print(f"{indent}    || {node.value}")  # Añadir tabulación adicional

def parse_and_print_ast(expression):
    expression = expression.strip()

    # Generar el árbol AST
    tree = ast.parse(expression, mode='eval')

    # Formatear y mostrar el árbol AST
    formatted_expression = format_node(tree.body)
    print("Expression:", formatted_expression)
    print("\nTree Structure:")
    print_ast(tree.body)
