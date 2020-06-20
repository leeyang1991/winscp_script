#!/usr/bin/python
# coding=gbk
"""
FTP常用操作
"""
from ftplib import FTP
import os
from tqdm import tqdm


class FTP_OP:
    def __init__(self, host, username, password, port):
        """
        初始化ftp
        :param host: ftp主机ip
        :param username: ftp用户名
        :param password: ftp密码
        :param port:  ftp端口 （默认21）
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def ftp_connect(self):
        """
        连接ftp
        :return:
        """
        ftp = FTP()
        ftp.set_debuglevel(0)  # 不开启调试模式
        ftp.connect(host=self.host, port=self.port)  # 连接ftp
        ftp.login(self.username, self.password)  # 登录ftp
        return ftp

    def download_file(self, ftp_file_path, dst_file_path):
        """
        从ftp下载文件到本地
        :param ftp_file_path: ftp下载文件路径
        :param dst_file_path: 本地存放路径
        :return:
        """
        if not os.path.isdir(dst_file_path):
            os.makedirs(dst_file_path)

        buffer_size = 10240  #默认是8192
        ftp = self.ftp_connect()
        print ftp.getwelcome()  #显示登录ftp信息
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
