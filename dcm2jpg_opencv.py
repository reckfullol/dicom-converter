# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import cv2
import dicom
import numpy as np


# def convert_file(dcm_file_path, jpg_file_path):
#     dicom_img = dicom.read_file(dcm_file_path)
#     dicom_img.WindowCenter = -400
#     dicom_img.WindowWidth = 1500
#     img = dicom_img.pixel_array
#     cv2.imwrite(jpg_file_path, img)

# def convert_file(dcm_file_path, jpg_file_path):
#     dicom_img = dicom.read_file(dcm_file_path)
#     img = dicom_img.pixel_array
#     window_center = -400
#     window_width = 1500
#     scaled_img = cv2.convertScaleAbs(img-window_center, alpha=(255.0 /window_width))
#     cv2.imwrite(jpg_file_path, scaled_img)

def convert_file(dcm_file_path, jpg_file_path):
    dicom_img = dicom.read_file(dcm_file_path)
    img = dicom_img.pixel_array
    scaled_img = cv2.convertScaleAbs(img-np.min(img), alpha=(255.0 / min(np.max(img)-np.min(img), 10000)))
    cv2.imwrite(jpg_file_path, scaled_img)

if __name__ == '__main__':
	
	rootdir = "D:\CT\A7"

	for parent, dirnames, filenames in os.walk(rootdir):
		for filename in filenames:
			if '.dcm' in filename.lower():
				dicom_path = os.path.join(parent, filename)
				name = dicom_path.replace('\\', '_')[3:]
				jpg_path = "d:\CT_JPG\\%s.jpg" % name
				print (jpg_path)
				convert_file(dicom_path, jpg_path)
