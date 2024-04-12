################################
# Name: Dorji Tshering
# Department: BE First Electrtical
# 02230062
################################
# REFERENCES
# http://coreyms.com/
# http://https//app.dataquest.io/c/79/m/452/reading-and-writing-to-files/1/reading-files-in-python
################################
# SOLUTION
# Your Solution Score:49801
# put your number here: 2
################################

def read_input(): #Defined a function named read_input 
    return open("input_2_cap1.txt", "r")# it returns the corresponding file object opened in read mode('r')

def calc_score(k):
    score_dict = {'A X': 3,  'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z': 9, 'C Z': 7} 
                   #Inatialized a dictionary named score_dict which store the combination of keys and values
    total_value = 0

    for line in k : #starts a loop that iterates over each line in the file
        value = line.strip() #each line is stripped of leading and trailing whitespace characters using the strip() method and assigns the result to the variable value

        value_from_dict = score_dict.get(value, None) # checks if the values exits as a key in dictionary and if there is it retrives the corresponding score from the dictionay and adds it to total_score
                                                       # if value doesn't exist it assigns 'none'
        if value_from_dict is not None:
            total_value += value_from_dict # 
    print("Total value:", total_value)#  prints total calcultaed score after processing all the line in the file

calc_score(read_input())# calls the function with the file object returned by the read_input function

