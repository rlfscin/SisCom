from math import exp, log, ceil

def qwt(tags):
    def get_ws(L, t):
        if t == 1 and last_L < L:
            return f(L)
        elif t != 1 and last_L < L:
            return last_ws
        elif t >= 0 and last_L >= L:
            return 1
        
    def f(L):
        return int(k * (1.0 - exp(-beta * L)))
        
    bits_reader = 0
    step_count = 0
    memory = []
    
    stack = ['1', '0']
    
    k = len(tags[0])
    ws_lenght = int(ceil(log(k, 2)))
    crc_lenght = 5
    beta = 0.5
    
    L = None
    ws = None
    t = None
    
    first_execution = True
    
    while len(stack) > 0:
        last_L = L
        last_ws = ws
        last_t = t
        
        prefix = stack.pop()
        step_count += 1
        L = len(prefix)
        
        bits_reader += L + ws_lenght
        
        if first_execution:
            ws = 1
            first_execution = False
        else:
            ws = get_ws(L, last_t)
        
        found_tags = [tag for tag in tags if tag.startswith(prefix)]
        t = len(found_tags)
        
        bits_tags += t * (ws + crc_lenght)
        
        if t > 1:
            stack.append(prefix + '1')
            stack.append(prefix + '0')
        elif t == 1 and L + ws < k:
            found_tag = found_tags[0]
            stack.append(prefix + found_tag[len(prefix) : len(prefix) + ws])
        elif t == 1 and L + ws >= k:
            memory.append(found_tags[0])
            pass

    return {"bits_reader": bits_reader, "bits_tags": bits_tags, "step_count": step_count}
    
