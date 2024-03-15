def sqlToJson(model, data):
    list = []
    
    for d in data:
        obj = {}
        i = 0
        
        for m in model:
            obj[m] = d[i]
            i = i + 1
            
        list.append(obj)
    return list