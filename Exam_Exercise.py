try:
    file_name=input("Please,enter your file name to proceed:")   #take input from user
    file_data=open(file_name) #opening file
    carbohydrates=list() #create empty list to add file data into
    amount_carbohydrates=0 #default is 0
    total_kilocalories=0 #default is 0
    number_bad_meals=0  #default is 0
    for each_line in file_data: #reading file
        carbohydrates.append(int(each_line.strip())) #converting to int and adding each number to list
    
    def num_of_calories(carbohydrates): #define a function to compute amount of kilocalories
        amount_carbohydrates=sum(carbohydrates) #find total amount of carbs.txt data
        total_kilocalories=amount_carbohydrates*4 #find total kilocalories ( 1gr carbohydrate =4 kkcal energy)
        return total_kilocalories #returning value to used furthermore
    
    
    total_kilocalories=num_of_calories(carbohydrates) #assign new value to variable that comes from function
    
    print("The number of kilocalories: {}".format(total_kilocalories))
    if total_kilocalories < 100 and total_kilocalories>=0:
        print("You can have some dessert (you have consumed less than 100 kilocalories with carbs today)")
    elif total_kilocalories > 100:
        print("You cannot have any dessert (you have consumed more than 100 kilocalories with carbs today)")
    elif total_kilocalories < 0: #it is additional to exercise to prevent negative kilocalories (I assume it is not possible)
        print("This result is not possible")
        
    
    for each_carbohydrate in carbohydrates:
        if each_carbohydrate>5: #to check if bigger than 5gr carbohydrates
            number_bad_meals+=1 #counting bad meals
            
    
    print("The number of bad meals today: {}".format(number_bad_meals))
        
except FileNotFoundError: #type of exception raises only if file name is wrong
    print("Please input existing file")
    