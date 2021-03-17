1- Launch Listener, it listens untill announcer connects
2- Launch P2P_Server
3- Launch Announcer, it announces the local files of users
4- Launch P2P Client. It asks for broadcasters (Owner of file we want to download) IP Address and name of the file we want to download.(Including file extension!)
5- Program downloads requested file under P2P_Client's directory.



LIMITATIONS:

Chunks doesn't work as in function_spec.pdf , users can't seed to another users
There is no try: except: structure. If there is an error, program just terminates. Doesn't throw any exceptions.