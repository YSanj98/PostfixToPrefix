class TreeNode:
    def __init__(self, value):
        """
        Constructor which sets the value, left and right attributes of the class.
        """

        self.value = value
        self.left = None
        self.right = None


def is_operand(c):
    """
    Check if a character is an operand or not.
    """
    return bool(c.isalpha())


def postfixtoprefix(post):
    """
    Convert a postfix expression to a prefix expression by iterating through the characters in the postfix expression,
    and using a stack to keep track of the operands and operators.
    """
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
    """
    Recursively print out the prefix expression by traversing the tree in a pre-order fashion.
    """
    if rootelement:
        print(rootelement.value, end="")
        print_prefix_expression(rootelement.right)
        print_prefix_expression(rootelement.left)

try:
    """
    Exception Handling
    """
    postfix = input("Enter a valid postfix expression: ")
    print("Postfix expression: ", postfix)
    root = postfixtoprefix(postfix)
    print("Prefix expression: ", end="")
    print_prefix_expression(root)
except Exception as e:
    print("An error occured: ", e)
