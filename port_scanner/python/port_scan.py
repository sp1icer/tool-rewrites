#!/usr/bin/env python3
import argparse
import socket


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
        # TODO: Figure out how to thread this for better performance.
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
    parser = argparse.ArgumentParser(description='Conducts a port scan of the listed targets.')
    targets = parser.add_mutually_exclusive_group()
    parser.add_argument("-p", "--ports", type=str, help='Ports that need to be scanned.')
    targets.add_argument("-l", "--list", type=str, help="Path to a list of target addresses or host names.")
    targets.add_argument("-H", "--host", type=str, help="A single target to be scanned.")
    # TODO: Add a threading argparse once I've worked out how to thread a class method.
    args = parser.parse_args()
    host_list = []
    if args.host:
        host_list.append(args.host)
    else:
        # TODO: Add in functionality to parse a text list of hosts and add to host_list array.
        pass
    # TODO: Add in ability to take in port lists, both on command line and via file.
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
