# image-renamer

Helper to rename files from a game cam based on when the picture was taking, using the [EXIF metadata](https://en.wikipedia.org/wiki/Exif).

## Usage

1. open a terminal to the folder containing images you want to rename
2. `docker run --rm -v "$PWD:/app/images" ghcr.io/lazy-electron-consulting/image-renamer /app/images`

You can pass `--help` to see other options.
