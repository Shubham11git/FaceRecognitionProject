import requests
import os

def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {destination}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def download_images(username, repo_name, path, branch='main'):
    base_url = f'https://api.github.com/repos/{username}/{repo_name}/contents/{path}?ref={branch}'
    response = requests.get(base_url)

    if response.status_code == 200:
        contents = response.json()
        for item in contents:
            if item['type'] == 'file' and item['name'].lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                download_url = item['download_url']
                destination = os.path.join('downloaded_images', item['name'])
                download_file(download_url, destination)
    else:
        print(f"Failed to retrieve directory contents. Status code: {response.status_code}")

# Replace these with your GitHub username, repository name, and directory path
username = 'Shubham11git'
repo_name = 'FaceRecognitionProject'
directory_path = 'images'

# Create a directory to store the downloaded images
os.makedirs('downloaded_images', exist_ok=True)

download_images(username, repo_name, directory_path)
