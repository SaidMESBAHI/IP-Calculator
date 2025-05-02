def valid_ip(ip):
    try:
        parts = ip.strip().split('.')
        return len(parts) == 4 and all(0 <= int(part) <= 255 for part in parts)
    except:
        return False

def valid_cidr(cidr):
    try:
        cidr = int(cidr)
        return 0 <= cidr <= 32
    except:
        return False

def valid_mask(mask):
    try:
        parts = list(map(int, mask.strip().split(".")))
        if len(parts) != 4:
            return False
        return all(0 <= part <= 255 for part in parts)
    except:
        return False

def mask_to_cidr(mask):
    try:
        binary_str = ''.join(f'{int(part):08b}' for part in mask.split('.'))
        if '01' in binary_str:
            return None
        return str(binary_str.count('1'))
    except:
        return None
