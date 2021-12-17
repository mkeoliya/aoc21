from functools import reduce

with open('input.txt') as f:
    input = f.read().splitlines()[0]
    bits = list("".join(bin(int(c, 16))[2:].zfill(4) for c in input.strip()))


pyint = int


def int(x, y=10):
    return pyint("".join(x), y)


def parse(k):
    version = int(k[:3], 2)
    k[:] = k[3:]
    typeid = int(k[:3], 2)
    k[:] = k[3:]
    if typeid == 4:
        data = []
        while True:
            cont = k.pop(0)
            data += k[:4]
            k[:] = k[4:]
            if cont == "0":
                break
        data = int(data, 2)
        return (version, typeid, data)
    else:
        packets = []
        if k.pop(0) == "0":
            length = int(k[:15], 2)
            k[:] = k[15:]
            d = k[:length]
            k[:] = k[length:]
            while d:
                packets.append(parse(d))
        else:
            num = int(k[:11], 2)
            k[:] = k[11:]
            for _ in range(num):
                packets.append(parse(k))
        return (version, typeid, packets)


def eval(packet):
    op = packet[1]
    if op == 4:
        return packet[2]

    vals = list(map(eval, packet[2]))
    if op == 0:
        return sum(vals)
    elif op == 1:
        return reduce(lambda x, y: x * y, vals)
    elif op == 2:
        return min(vals)
    elif op == 3:
        return max(vals)
    elif op == 5:
        return 1 if vals[0] > vals[1] else 0
    elif op == 6:
        return 1 if vals[0] < vals[1] else 0
    elif op == 7:
        return 1 if vals[0] == vals[1] else 0


q = parse(bits)

print(eval(q))
