class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to track opening brackets
        stack = []
        # Map each closing bracket to its corresponding opening bracket
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        # Process each character in the string
        for c in s:
            # If the character is a closing bracket
            if c in closeToOpen:
                # Check if stack has elements AND top matches the expected opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # Valid match - pop the opening bracket from stack
                    stack.pop()
                else:
                    # Invalid: either stack is empty (no opening bracket)
                    # OR top doesn't match expected opening bracket
                    return False
            else:
                # Character is an opening bracket - push onto stack
                stack.append(c)
        
        # After processing all characters, check if stack is empty
        # Empty stack = all brackets were properly matched
        return True if not stack else False