import random
import string

OUTPUT_FILE = "large_random_text.txt"
FILE_SIZE_MB = 1024        # Size of file to generate (e.g. 1024 = 1GB)
CHUNK_SIZE = 1024 * 1024   # 1MB per write

def random_text(length):
    chars = string.ascii_letters + string.digits + "     \n"
    return ''.join(random.choices(chars, k=length))

def generate_large_file():
    total_bytes = FILE_SIZE_MB * 1024 * 1024
    written = 0

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        while written < total_bytes:
            chunk = random_text(min(CHUNK_SIZE, total_bytes - written))
            f.write(chunk)
            written += len(chunk)

    print(f"Generated {OUTPUT_FILE} ({FILE_SIZE_MB} MB)")

if __name__ == "__main__":
    generate_large_file()