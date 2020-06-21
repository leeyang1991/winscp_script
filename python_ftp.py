#!/usr/bin/python
# coding=gbk
"""
FTP���ò���
"""
from ftplib import FTP
import os
from tqdm import tqdm


class FTP_OP:
    def __init__(self, host, username, password, port):
        """
        ��ʼ��ftp
        :param host: ftp����ip
        :param username: ftp�û���
        :param password: ftp����
        :param port:  ftp�˿� ��Ĭ��21��
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def ftp_connect(self):
        """
        ����ftp
        :return:
        """
        ftp = FTP()
        ftp.set_debuglevel(0)  # ����������ģʽ
        ftp.connect(host=self.host, port=self.port)  # ����ftp
        ftp.login(self.username, self.password)  # ��¼ftp
        return ftp

    def download_file(self, ftp_file_path, dst_file_path):
        """
        ��ftp�����ļ�������
        :param ftp_file_path: ftp�����ļ�·��
        :param dst_file_path: ���ش��·��
        :return:
        """
        if not os.path.isdir(dst_file_path):
            os.makedirs(dst_file_path)

        buffer_size = 10240  #Ĭ����8192
        ftp = self.ftp_connect()
        print ftp.getwelcome()  #��ʾ��¼ftp��Ϣ
        file_list = ftp.nlst(ftp_file_path)
        # print dst_file_path
        # print file_list
        # exit()
        for file_name in tqdm(file_list):
            try:
                file_name = file_name.split('/')[-1]
                ftp_file = ftp_file_path + file_name
                write_file = dst_file_path + '/' +file_name
                if not os.path.exists(write_file):
                    with open(write_file, "wb") as f:
                        ftp.retrbinary('RETR {0}'.format(ftp_file), f.write, buffer_size)
                        f.close()
            except Exception as e:
                print e
        ftp.quit()

if __name__ == '__main__':
    host = "192.168.0.100"
    username = "***"
    password = "***"
    port = "21"
    ftp_file_path = "/home/pic/"
    dst_file_path = "F:/pic/"
    ftp = FTP_OP(host=host, username=username, password=password, port=port)
    ftp.download_file(ftp_file_path=ftp_file_path, dst_file_path=dst_file_path)