import yt_dlp
import os

def download(url, output_dir="."):
    """Downloads YouTube audio and saves it to the specified output directory.

    Args:
        url (str): The URL of the YouTube video to download.
        output_dir (str, optional): The directory where the downloaded audio file
            will be saved. Defaults to the current working directory (".").

    Raises:
        OSError: If the output directory does not exist or is not writable.
        yt_dlp.utils.DownloadError: If there's an error during the download process.
    """

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Custom output template
    }

    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed! Audio saved to: {output_dir}")

    except OSError as e:
        print(f"Error creating output directory: {e}")
    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")

if __name__ == "__main__":
    output_dir = "audio"
    url = input("Enter the URL of the video: ")
    download(url, output_dir.strip())  # Remove leading/trailing whitespace from output_dir