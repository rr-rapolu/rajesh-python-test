import unittest

def justify_text(paragraph, page_width):
    # Validate input types
    if not isinstance(paragraph, str):
        raise TypeError("Paragraph must be a string")
    if not isinstance(page_width, int):
        raise TypeError("Page width must be an integer")
    if page_width <= 0:
        raise ValueError("Page width must be greater than 0")
    
    # Split the paragraph into words
    words = paragraph.split()
    lines = []
    current_line = []
    current_length = 0

    # Split words into lines based on the page width
    for word in words:
        if current_length + len(word) + len(current_line) > page_width:
            lines.append(current_line)
            current_length = 0
            current_line = []
        current_line.append(word)
        current_length += len(word)

    if current_line:
        lines.append(current_line)

    # Justify each line except the last one
    justified_lines = []
    for line in lines:
        total_spaces = page_width - sum(len(word) for word in line)
        gaps_count = len(line) - 1
        
        if gaps_count > 0:
            space_between_words, extra_spaces = calculate_spaces(total_spaces, gaps_count)
            justified_line = create_justified_line(line, space_between_words, extra_spaces)
        else:
            justified_line = line[0] + ' ' * (page_width - len(line[0]))
        justified_lines.append(justified_line)
    
    return justified_lines

def calculate_spaces(total_spaces, gaps_count):
    # Calculate spaces between words and extra spaces
    space_between_words = total_spaces // gaps_count
    extra_spaces = total_spaces % gaps_count
    return space_between_words, extra_spaces

def create_justified_line(line, space_between_words, extra_spaces):
    # Create a justified line by adding spaces between words
    justified_line = ""
    for i, word in enumerate(line[:-1]):
        justified_line += word
        justified_line += ' ' * (space_between_words + (1 if i < extra_spaces else 0))
    justified_line += line[-1]
    return justified_line

page_width = 20
paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
justified_text = justify_text(paragraph, page_width)
for line in justified_text:
    print(f"'{line}'")

class TestJustifyText(unittest.TestCase):
    def test_single_word(self):
        paragraph = "Hello"
        page_width = 10
        expected_output = ["Hello     "]
        self.assertEqual(justify_text(paragraph, page_width), expected_output)

    def test_multiple_words_single_line(self):
        paragraph = "Hello world"
        page_width = 20
        expected_output = ["Hello          world"]
        self.assertEqual(justify_text(paragraph, page_width), expected_output)

    def test_multiple_words_multiple_lines(self):
        paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
        page_width = 20
        expected_output = [
            "This   is  a  sample",
            "text      but      a",
            "complicated  problem",
            "to  be solved, so we",
            "are adding more text",
            "to   see   that   it",
            "actually      works."
        ]
        self.assertEqual(justify_text(paragraph, page_width), expected_output)

    def test_invalid_page_width(self):
        paragraph = "This is a sample text."
        page_width = 0  # Invalid page width
        with self.assertRaises(ValueError):
            justify_text(paragraph, page_width)

    def test_invalid_paragraph(self):
        paragraph = 123  # Invalid paragraph
        page_width = 20
        with self.assertRaises(TypeError):
            justify_text(paragraph, page_width)

    def test_empty_paragraph(self):
        paragraph = ""
        page_width = 20
        expected_output = []
        self.assertEqual(justify_text(paragraph, page_width), expected_output)

if __name__ == "__main__":
    unittest.main()
