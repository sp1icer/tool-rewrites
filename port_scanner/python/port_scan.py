#!/usr/bin/env python3
import argparse
import socket

parser = argparse.ArgumentParser(description='Conducts a port scan of the listed targets.')


class HostClass:
    def __init__(self):
        self.host = "scanme.nmap.org"
        self.ports = []
        self.results = self.ResultsClass()

    class ResultsClass:
        def __init__(self):
            self.open_ports = []
            self.closed_ports = []


def conn_scan(host_object):
    """
    Connects to the host on the port given.
    :param: HostClass object to parse hosts/ports from and connect with.
    :return: 0 for success, 1 for error/failure.
    """
    for host in host_object.valid_hosts:
        for port in host_object.ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                s.close()
                print('[+] Socket connected! ' + str(host + ":" + str(port)))

            except:



def resolve_host(host_list):
    """
    Handles conversion of hostname to IPV4 addresses for all hosts in list.
    :param host_list: List of hosts to convert.
    :return: Hosts object that contains list of ports, valid, and invalid hosts.
    """
    hosts = HostClass()
    for host in host_list:
        try:
            hosts.valid_hosts.append(socket.gethostbyname(host))
        except Exception as e:
            hosts.invalid_hosts.append(host)
    return hosts


def main():
    host_list = ['scanme.nmap.org']
    port_list = [80, 443]
    host_object = resolve_host(host_list)
    host_object.ports = port_list
    conn_scan(host_object)


if __name__ == "__main__":
    main()
