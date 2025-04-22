import instaloader

def download_instagram_post(post_url):

    loader = instaloader.Instaloader()

    try:
       
        parts = post_url.rstrip('/').split('/')
     
        shortcode = parts[-2]
    except Exception as e:
        print(f"Error extracting shortcode: {e}")
        return

    try:
       
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        
      
        loader.download_post(post, target="downloads")
        print(f"✅ Successfully downloaded post: {shortcode}")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"❌ Failed to download post: {e}")

if __name__ == "__main__":
    url = input("Enter Instagram post URL: ").strip()
    download_instagram_post(url)