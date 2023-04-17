import threading
import queue
import pexpect


inventory_list = [["192.168.1.1", "user", "password"], ["192.168.1.2", "user", "password"], ["192.168.1.3", "user", "password"]]


def ssh_into_device(host_info):
    # Perform SSH using pexpect
   # try: 
   #     ssh_session = pexpect.spawn("ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-rsa " + username + "@" + host)
   #     ssh_session.expect("Password:")
   #     ssh_session.sendline(password)
   #     ssh_session.expect(">")
   #     session_info = ssh_session.before.decode('utf-8')
   # except pexpect.EOF:
   #     session_info = "ERROR: EOF"
   # except pexpect.TIMEOUT:
   #     session_info = "ERROR: TIMEOUT")
   # return session_info

    x = host_info[0] + host_info[1] + host_info[2]

    return x


def connect(q):
    while True: 
        try:
            host_info = q.get()
            info = ssh_into_device(host_info)
            print(info)
        except:
            pass
        q.task_done()


def main():
    q = queue.Queue()

    for host_info in inventory_list:
        q.put(host_info)

    # Create the threads
    stop_event = threading.Event()
    for i in range(2):
        t = threading.Thread(target=connect, args=(q,))
        t.daemon = True
        t.start()
    q.join()

if __name__ == "__main__":
    main()

