import math
import cv2
from collections import defaultdict
import csv
import os
import sys


def convert(path, output, opt):
    if opt > 0:
        files = os.listdir(path)
        file_idx = 0
        res_list = list()
        for file in sorted(files):
            print(f'Reading {file} ...')
            if file[-3:] != 'csv':
                print(f'{file} is skipped because it is not csv file.')
                continue

            with open(f'{path}/{file}') as my_csv:
                csv_mapping_list = list(csv.DictReader(my_csv))

            total_num = len(csv_mapping_list)
            for cur_line in csv_mapping_list:
                res_list.append({'timestep': int(cur_line['timestep']),
                                 'id': int(cur_line['id']),
                                 'left': float(cur_line['left']) + opt/2,
                                 'top': float(cur_line['top']) + opt/2,
                                 'height': opt,
                                 'width': opt,
                                 'img_height': int(cur_line['img_height']),
                                 'img_width': int(cur_line['img_width']),
                                 'parent': int(cur_line['parent'])
                                 })
            break

        with open(f'{output}.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(res_list[0].keys()))
            writer.writeheader()

            for row in res_list:
                writer.writerow(row)
            csvfile.flush()
    else:
        print("Input error.")
        sys.exit()


if __name__ == '__main__':
    print('[input path]: ')
    file_path = input()
    print('[output path]: ')
    output_path = input()
    print("Input directory path: " + file_path)
    print("Box width (= height>0): ")
    opt = int(input())

    convert(file_path, output_path, opt)