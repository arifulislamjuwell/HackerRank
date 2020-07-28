
def timeConversion(s):
    split= s[:-2].split(':')
    hour, min, sec= int(split[0]), int(split[1]), int(split[2])
    if s[-2:] == 'PM':
        if hour == 12:
            return ':'.join(split)
        else:
            split[0]= str(int(split[0])+ 12)
            return ':'.join(split)
        split[0]= int(split[0])+ 12
    else:
        if hour == 12:
            split[0]= '00'
            return ':'.join(split)
        else:
            return s[:-2]

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)
