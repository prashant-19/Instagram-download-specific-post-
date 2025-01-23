import requests
import os

def fetch_json_data(instagram_url):
    try:
        json_url = instagram_url.strip('/') + '/?__a=1&__d=dis'

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(json_url, headers=headers)
        response.raise_for_status()  

        return response.json()
    except Exception as e:
        print(f"Error fetching JSON from {instagram_url}: {e}")
        return None

def download_video_from_json(json_data, save_path):
    try:
        video_url = json_data["graphql"]["shortcode_media"]["video_url"]

        response = requests.get(video_url, stream=True)
        response.raise_for_status()

        with open(save_path, "wb") as video_file:
            for chunk in response.iter_content(chunk_size=1024):
                video_file.write(chunk)

        print(f"Video downloaded successfully: {save_path}")
    except KeyError:
        print("Video URL not found in the JSON data.")
    except Exception as e:
        print(f"Error downloading video: {e}")

def process_instagram_links(links, download_folder="downloads"):
    os.makedirs(download_folder, exist_ok=True)

    for index, link in enumerate(links):
        print(f"Processing link {index + 1}/{len(links)}: {link}")

        json_data = fetch_json_data(link)

        if json_data:
            video_filename = os.path.join(download_folder, f"video_{index + 1}.mp4")

            download_video_from_json(json_data, video_filename)

if __name__ == "__main__":
    instagram_links = [
        "https://www.instagram.com/p/C_K4TszBBr_/",
        "https://www.instagram.com/p/DBJInnjh34u/",
        "https://www.instagram.com/p/DENUeOOhIVg/"
    ]

    process_instagram_links(instagram_links)
