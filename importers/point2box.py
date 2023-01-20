import math
import cv2
from collections import defaultdict
import csv
import os
import sys


def convert(path, output, opt):
    if opt <= 0:
        files = os.listdir(path)
        num_timestep = len(files) - opt + 1

        res = dict()
        for file in sorted(files):
            print(f'Reading {file} ...')
            if file[-3:] != 'tif':
                print(f'{file} is skipped because it is not tif file.')
                continue
            arr = cv2.imread(f'{path}/{file}', -1)
            arr_map = defaultdict(list)
            time_dict = dict()
            img_height = len(arr)
            img_width = len(arr[0])
            for j in range(len(arr)):
                for i in range(len(arr[j])):
                    if arr[j][i] != 0:
                        arr_map[arr[j][i]].append((i, j))

            for key in arr_map.keys():
                x_list = list(map(lambda x: x[0], arr_map[key]))
                y_list = list(map(lambda x: x[1], arr_map[key]))
                min_x, max_x, min_y, max_y = min(x_list), max(x_list), min(y_list), max(y_list)
                time_dict[key] = [min_x, max_x, min_y, max_y]

            digits = int(math.log10(num_timestep))
            timestep = int(file[-4 - digits - 1:-4])
            if timestep in res:
                print('timestep is duplicated')
            res[timestep] = time_dict

        res_list = list()
        for t in sorted(res.keys()):
            if t > 0:
                for i in sorted(res[t].keys()):
                    res_list.append({'timestep': t+1,
                                     'id': i,
                                     'left': res[t][i][0],
                                     'top': res[t][i][3],
                                     'height': res[t][i][3] - res[t][i][2],
                                     'width': res[t][i][1] - res[t][i][0],
                                     'img_height': img_height,
                                     'img_width': img_width,
                                     'parent': 0})
        with open(f'{output}.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(res_list[0].keys()))
            writer.writeheader()

            if opt == 2:
                parent_dict = dict()
                with open(f'{path}/man_track.txt', 'r') as trackfile:
                    for line in trackfile.readlines():
                        line = list(map(int, line.split()))
                        parent_dict[line[0]] = line[3]
                for res in res_list:
                    res['parent'] = parent_dict[res['id']]
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
    print("Box width (= height): ")
    opt = int(input())

    convert(file_path, output_path, opt)