import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import re
import tiktoken




book = epub.read_epub("Ego_Is_the_Enemy_Ryan_Holiday_Z-Library.epub")

items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

chapters = []

items=book.get_items_of_type(ebooklib.ITEM_DOCUMENT)
for item in items:
    if 'GlobalBackad' in item.get_name() or "navDoc" in item.get_name() or "Cover" in item.get_name():
        continue
    else:
        chapters.append(item)

def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    chapter = ''.join(text)
    chapter_word_size = len(re.findall(r'\w+', chapter))
    chapter_token_size = num_tokens_from_string(chapter, "gpt-3.5-turbo")
    return chapter, chapter_word_size, chapter_token_size

def num_tokens_from_string(string: str, model: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(string))
    return num_tokens

texts = {}
for c in chapters:
    texts[c.get_name()] = chapter_to_str(c)

sum_of_tokens = 0

for text in texts:


    sum_of_tokens = sum_of_tokens + texts[text][2]


max_input_length = 4096  # The maximum length of input that GPT-3.5-turbo can handle

chunks = []
current_chunk = ""

for text in texts:
    
    chunk_size = num_tokens_from_string(current_chunk, "gpt-3.5-turbo")

    # Check if the current chapter would cause the current chunk to exceed the maximum input length
    if chunk_size + texts[text][2] > max_input_length:
        # If so, add the current chunk to the list of chunks and start a new chunk
        chunks.append(current_chunk)
        current_chunk = ""

    # Add the current chapter to the current chunk
    current_chunk += texts[text][0] + "\n"

# Add the final chunk to the list of chunks
if current_chunk:
    chunks.append(current_chunk)

for chunk in chunks:
    print(num_tokens_from_string(chunk, "gpt-3.5-turbo"))