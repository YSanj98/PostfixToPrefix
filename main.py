class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_operand(c):
    return bool(c.isalpha())


def postfixtoprefix(post):
    stack = []
    for c in post:
        if is_operand(c):
            op = TreeNode(c)
            stack.append(op)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            expression = TreeNode(c)
            expression.left = op1
            expression.right = op2
            stack.append(expression)
    return stack.pop()


def print_prefix_expression(rootelement):
    if rootelement:
        print(rootelement.value, end="")
        print_prefix_expression(rootelement.right)
        print_prefix_expression(rootelement.left)


postfix = input("Enter a valid postfix expression: ")
print("Postfix expression: ", postfix)
root = postfixtoprefix(postfix)
print("Prefix expression: ", end="")
print_prefix_expression(root)

