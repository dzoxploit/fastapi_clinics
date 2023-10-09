def sequenceExist(main, seq):
    main_length = len(main)
    seq_length = len(seq)
    
    for i in range(main_length - seq_length + 1):
        subarray = main[i:i+seq_length]
        
        if subarray == seq:
            return True
            
    return False

main = [20, 7, 8, 10, 2, 5, 6]
print(sequenceExist(main, [7, 8]))  
print(sequenceExist(main, [8, 7]))  
print(sequenceExist(main, [7, 10]))  