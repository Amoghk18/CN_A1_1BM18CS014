queue = list(map(int, input("Enter the packet sizes as space separated numbers: ").split(" ")))
out_rate = int(input("Enter output rate: "))
storage = out_rate
i = 0
while queue:
    print("Packet number "+str(i)+", Packet size = "+str(queue[-1]))
    if queue[-1] < out_rate:
        out_rate -= queue[-1]
        x = queue.pop()
        print("Bucket output successfull")
        print("Last "+str(x)+" bytes sent")
    elif queue[-1] > out_rate:
        out_rate = storage
        if queue[-1] > out_rate:
            print("Bucket overflowed")
            break
        elif queue[-1] < out_rate:
            out_rate -= queue[-1]
            x = queue.pop()
            print("Bucket output successfull")
            print("Last "+str(x)+" bytes sent")
    else:
        queue.pop()
        print("Bucket output successfull")
        print("Last "+str(out_rate)+" bytes sent")
    i += 1