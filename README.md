
# Justify Text

This Python script justifies text to fit a specified page width by adding spaces between words.

## Usage

```python

# Example usage

page_width = 20

paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."

justified_text = justify_text(paragraph, page_width)

for line in justified_text:

    print(f"'{line}'")

```

## Running the Tests

You can run the tests using the following command:

```shell

python3 justify_text.py

```

## Running Individual Tests

You can run individual tests by specifying the test method. For example, to run the test_single_word test, use the following command

```sh

python3 -m  unittest  justify_text.TestJustifyText.test_single_word

```

## Tests

**test_single_word**: Tests justifying a single word.

**test_multiple_words_single_line**: Tests justifying multiple words in a single line.

**test_multiple_words_multiple_lines**: Tests justifying multiple words in multiple lines.

**test_invalid_page_width**: Tests handling invalid page width.

**test_invalid_paragraph**: Tests handling invalid paragraph input.

**test_empty_paragraph**: Tests handling an empty paragraph.


## Author

[Rajesh Kumar Reddy Rapolu](https://github.com/rr-rapolu)
