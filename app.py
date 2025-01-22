import instaloader

def download_instagram_posts(url_list):
    
    loader = instaloader.Instaloader()

    for url in url_list:
        try:
        
            shortcode = url.split("/")[-2]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            
            print(f"Downloading: {url}")
            loader.download_post(post, target=post.owner_username)
        except Exception as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":

    urls = [
        "https://www.instagram.com/p/C7CGwz_IGsL/"
        ]


    download_instagram_posts(urls)
