from pytube import YouTube
import os

def download_video():
    # Ask user for video URL and destination folder
    url = input("🔗 Enter the YouTube video URL: ").strip()
    destination = input("📁 Enter the destination folder path: ").strip()

    # Ensure destination folder exists
    if not os.path.exists(destination):
        print("📂 Folder not found. Creating it...")
        os.makedirs(destination)

    try:
        # Create YouTube object
        yt = YouTube(url)
        print(f"🎬 Video Title: {yt.title}")

        # Get highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(output_path=destination)
        print("✅ Download completed successfully!")

    except Exception as e:
        print("❌ Failed to download video.")
        print(f"Error: {e}")
        print("🔍 Please check if the URL is valid and try again.")

# Run the downloader
download_video()