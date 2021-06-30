class Token:
    TOP_LEFT = "┌"
    TOP_RIGHT = "┐"
    BOTTOM_LEFT = "└"
    BOTTOM_RIGHT = "┘"
    HORIZONTAL = "─"
    BOX_START = TOP_LEFT + HORIZONTAL
    VERTICAL = "│"
    INPUT_PORT = "┼"
    OUTPUT_PORT = "┼"
    FUNCTION = "ƒ"
    COMMENT = "/*...*/"
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'
    LEFT_PAREN = "("
    FUNCTION_START = FUNCTION + LEFT_PAREN
    RIGHT_PAREN = ")"
    KEYWORD_BRANCH = "[Branch]"
    KEYWORD_FOR_LOOP = "[For Loop]"
    KEYWORD_FOR_EACH = "[For Each]"
    KEYWORD_WHILE_LOOP = "[While Loop]"
    KEYWORD_RETURN = "[Return]"
    KEYWORD_SET = "[Set]"
    DATA_FLOW_PORT = "○"
    CONTROL_FLOW_PORT = "►"
