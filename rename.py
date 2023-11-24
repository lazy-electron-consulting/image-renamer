import os
import argparse
from datetime import datetime
import exifread

def get_image_capture_date(file_path, exif_tag='EXIF DateTimeOriginal'):
    with open(file_path, 'rb') as file:
        tags = exifread.process_file(file, stop_tag=exif_tag)
        if exif_tag in tags:
            capture_date = tags[exif_tag].values
            return datetime.strptime(capture_date, '%Y:%m:%d %H:%M:%S')

    return None

def rename_images(directory_path, exif_tag='EXIF DateTimeOriginal', dry_run=False):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            file_path = os.path.join(directory_path, filename)
            capture_date = get_image_capture_date(file_path, exif_tag)

            if capture_date:
                # Convert the capture date to ISO8601 format with timezone
                iso8601_date = capture_date.strftime('%Y%m%d_%H%M%S%z')

                new_filename = iso8601_date + os.path.splitext(filename)[1]
                new_file_path = os.path.join(directory_path, new_filename)
                if filename == new_filename:
                    continue

                if dry_run:
                    print(f'Dry Run: Would rename {filename} to {new_filename}')
                else:
                    os.rename(file_path, new_file_path)
                    print(f'Renamed: {filename} to {new_filename}')

def main():
    parser = argparse.ArgumentParser(description='Rename image files to ISO8601 date with timezone.')
    parser.add_argument('directory_path', help='Path to the directory containing the image files')
    parser.add_argument('--exif_tag', default='EXIF DateTimeOriginal', help='EXIF tag to read for capture date')
    parser.add_argument('--dry-run', action='store_true', help='Print rename actions without actually renaming files')

    args = parser.parse_args()
    directory_path = args.directory_path
    exif_tag = args.exif_tag
    dry_run = args.dry_run

    if not os.path.exists(directory_path):
        print(f"Error: The specified directory '{directory_path}' does not exist.")
        return

    rename_images(directory_path, exif_tag, dry_run)

if __name__ == "__main__":
    main()
