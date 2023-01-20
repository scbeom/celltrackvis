import os
from PIL import Image
from pathlib import Path


def tif2jpg(path, out_path, px_sc):
    files = os.listdir(path)

    Path(out_path + "/converted").mkdir(parents=True, exist_ok=True)
    for file in files:
        if file[-3:] == 'tif':
            print(f'converting {file}...')

            outfile = out_path + f'/converted/{file[:-3]}jpg'
            im = Image.open(f"{path}/{file}")

            im.point(lambda i: i * (px_sc / 256)).convert('L').save(outfile, "JPEG", quality=100)
        else:
            print(f'{file} is skipped because it is not tif file.')
            continue


if __name__ == '__main__':
    print('[input path]: ')
    file_path = input()
    print('[output path]: ')
    output_path = input()
    print('[pixel scale] (0<): ')
    pixel_scale = int(input())
    print("TIF(F) directory path : " + file_path)

    tif2jpg(file_path, output_path, pixel_scale)