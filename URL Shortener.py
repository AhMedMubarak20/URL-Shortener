import hashlib

def generate_short_url(url):
    hashed = hashlib.md5(url.encode())
    return hashed.hexdigest()[:6]

original_url = input("Enter the original URL: ")
short_url = generate_short_url(original_url)
print(f"Shortened URL: https://short.url/{short_url}")
