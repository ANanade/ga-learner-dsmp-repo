# --------------
##File path for the file 
file_path 

def read_file(path):
    path= open(file_path, mode='r')
    for line in path.readlines():
        sentence= line
    return sentence
    
#sample_message=

sample_message=read_file(file_path)

print(sample_message)
#Code starts here




# --------------
#Code starts here

file_path_1
file_path_2


s= open(file_path_1, mode='r')
p= open(file_path_2, mode='r')
 
for line in s.readlines():
    message_1=line
    print(message_1)

for line in p.readlines():
    message_2=line
    print(message_2)


  
def fuse_msg(message_a, message_b):
    quotient=int(message_b)//int(message_a)
    return quotient

secret_msg_1=str(fuse_msg(message_1,message_2))

print(secret_msg_1)






# --------------
#Code starts here
file_path_3

s= open(file_path_3, mode='r')


for line in s.readlines():
    message_3=line
    print(message_3)


def substitute_msg(message_c):
    if message_c == 'Red':
        sub = 'Army Genera'
        return sub
    elif message_c== 'Green' :
        sub = 'Data Scientist'
        return sub
    elif message_c == 'Blue':
        sub ='Marine Biologist'
        return sub


secret_msg_2=str(substitute_msg(message_3))
print(secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

s= open(file_path_4, mode='r')
p= open(file_path_5, mode='r')
 
for line in s.readlines():
    message_4=line
    print(message_4)

for line in p.readlines():
    message_5=line
    print(message_5)


def compare_msg(message_d,message_e):
    a_list= message_d.split()
    b_list= message_e.split()
    c_list=[i for i in a_list if i not in b_list] 
    final_msg= " ".join(c_list)
    return final_msg

secret_msg_3=str(compare_msg(message_4,message_5))
print(secret_msg_3)



# --------------
#Code starts here
path= open(file_path_6, mode='r')


for line in path.readlines():
    message_6=line
    print(message_6)

def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list=message_f.split()
    
    #Creating the lambda function to identify even length words
    even_word=lambda x: (len(x)%2==0)
    
    #Splitting the message into a list
    b_list=(filter(even_word, a_list))
    
    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(b_list)
    
    #Returning the sentence
    return final_msg

#Calling the function to read file


#Calling the function 'filter_msg'
secret_msg_4=extract_msg(message_6)

#Printing the secret message
print(secret_msg_4)

#Code ends here








# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg=' '.join(message_parts)
print(secret_msg)

def write_file(secret_msg,path):
    a=open(path, 'a+')
    a.write(secret_msg)
    a.close()
final_path= user_data_dir + '/secret_message.txt'
q=(write_file(secret_msg,final_path))
print(q)
    #return secret_msg






