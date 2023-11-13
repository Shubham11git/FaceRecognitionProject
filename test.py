import requests

def get_image_urls(username, repo_name, path, branch='main'):
    base_url = f'https://api.github.com/repos/{username}/{repo_name}/contents/{path}?ref={branch}'
    response = requests.get(base_url)

    if response.status_code == 200:
        contents = response.json()
        image_urls = []
        for item in contents:
            if item['type'] == 'file' and item['name'].lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                raw_url = item['download_url'].replace('/downloads/', '/raw/')  # Convert download_url to raw_url
                image_urls.append(raw_url)
        return image_urls
    else:
        print(f"Failed to retrieve directory contents. Status code: {response.status_code}")
        return None

# Replace these with your GitHub username, repository name, and directory path
username = 'Shubham11git'
repo_name = 'FaceRecognitionProject'
directory_path = 'images'

image_urls = get_image_urls(username, repo_name, directory_path)

if image_urls:
    for url in image_urls:
        print(f"Image URL: {url}")
