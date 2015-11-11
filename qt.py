def qt(tags):
    queue = ['0', '1']
    #memory = []
    
    TAG_ID_LENGHT = len(tags[0])

    bits_reader = 0
    bits_tags = 0
    
    while len(queue) > 0:
        prefix = queue.pop(0)
    
        found_tag = None
        
        found_tags = [tag for tag in tags if tag.startswith(prefix)]
        
        bits_reader += len(prefix)
        bits_tags += len(found_tags) * TAG_ID_LENGHT
        
        if len(found_tags) == 1:
            #memory.append(found_tags[0])
            pass
        elif len(found_tags) > 1:
            queue.append(prefix + '0')
            queue.append(prefix + '1')
    return {"bits_reader": bits_reader, "bits_tags": bits_tags}
        
