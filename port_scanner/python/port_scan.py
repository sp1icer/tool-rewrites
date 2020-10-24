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

    def resolve_host(self, hostname):
        try:
            self.host = str(socket.gethostbyname(hostname))
        except:
            return

    def conn_scan(self):
        for port in self.ports:
            try:
                socket.setdefaulttimeout(1)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.host, port))
                self.results.open_ports.append(port)
            except:
                self.results.closed_ports.append(port)
            finally:
                s.close()


def main():
    host_list = ['scanme.nmap.org']
    port_list = [22, 25, 53, 80, 443]
    hosts = []
    for host in host_list:
        host_object = HostClass()
        host_object.ports = port_list
        host_object.host = host
        host_object.conn_scan()
        hosts.append(host_object)

    for host_object in hosts:
        print('[+] Results for host %s' % host_object.host)
        print('[+] Open ports: ')
        for open_port in host_object.results.open_ports:
            print('\t' + str(open_port))
        print('[+] Closed ports: ')
        for closed_port in host_object.results.closed_ports:
            print('\t' + str(closed_port))


if __name__ == "__main__":
    main()
