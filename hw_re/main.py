import re

# 1 Task: Find all words in a string that start with a capital letter.
# "Hello world, this is a Regex example with Python."

first = "Hello world, this is a Regex example with Python."
pattern1 = re.compile(r"[A-Z]\w+")
print(re.findall(pattern1, first))

# 2 Task: Replace all instances of "is" with "was" in the string.
# "This is a test. This is only a test."
second = "This is a test. This is only a test."
pattern2 = re.compile(r"\bis\b")
print(re.sub(pattern2, 'was', second))

# 3 Task: Extract All URLs from a Text
# Visit https://www.example.com or follow http://example.org.
# You can also check out https://another-example.com/path?arg=val for more details.
third = '''Visit https://www.example.com or follow http://example.org.
You can also check out https://another-example.com/path?arg=val for more details.'''
pattern3 = re.compile(r"\bhttp\S+[^.\s]+")
print(re.findall(pattern3, third))

# 4 Task: Find all hashtags in a comment
# "Loving the #sunset and #nature! #beautiful_day"
fourth = "Loving the #sunset and #nature! #beautiful_day"
pattern4 = re.compile(r'#[a-z_]+')
print(re.findall(pattern4, fourth))

# 5 Task: Remove the repeated words
# "This is is a test test string."
fifth = "This is is a test test string."
print(re.sub(r'\b(\w+)\s+\1\b', r'\1', fifth))
