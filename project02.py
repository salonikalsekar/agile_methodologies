#Initializing lists for the level 0,1,2
tagDatasWithLevel0 = ["HEAD","TRLR","NOTE"] 
tagDatasWithLevel1 = ["NAME","BIRT","SEX","DIV","FAMC","CHIL","MARR","HUSB","WIFE","FAMS","DEAT"]
tagDatasWithLevel2 = "DATE" 

#Initializing list for the level 0 tagDatas with IDs
level0WithIDS = ["INDI","FAM"]

#Contains the data that is read
gedcomList = []

#The gedcom file path is initialized and read
gedFile = open("C:\Users\salon\Desktop\Project02\MyFamilyTree.ged","r")

#While reading each line the line is processed till there is no line left
for data in gedFile:
    
    gedcomList = data.strip().split(" ")
    level =gedcomList[0]
    print("-->" + data) #for the format given

    
    
    #For level 2
    #if the current tag exists in the tagDatasWithLevel2 list, then the tag is valid
    if level == "2":
        if gedcomList[1] == tagDatasWithLevel2:
            tagData = gedcomList[1]
            print("<--" + level + "|" + tagData + "|" + "Y" + "|" + " ".join(gedcomList[2:]))
        else:
            tagData =gedcomList[1]
            print("<--" + level + "|" + tagData + "|" + "N" + "|" + " ".join(gedcomList[2:]))


    #For level 1
    #if the current tag exists in the tagDatasWithLevel1 list, then the tag is valid                     
    if level == "1":
        if gedcomList[1] in tagDatasWithLevel1:
            tagData =gedcomList[1]
            print("<--"+ level + "|" + tagData + "|" + "Y" + "|" + " ".join(gedcomList[2:]))
        else:
            tagData =gedcomList[1]
            print("<--"+ level + "|" + tagData + "|" + "N" + "|" + " ".join(gedcomList[2:]))


    #For level 0
    #if the current tag exists in the tagDatasWithLevel3 list, then the tag is valid
    if level == "0":
        if gedcomList[1] in tagDatasWithLevel0:
            tagData = gedcomList[1]
            print("<--" + level + "|" + tagData + "|" + "Y" + "|" + " ".join(gedcomList[2:]))
        elif gedcomList[2] in level0WithIDS:
            tagData = gedcomList[2]
            id = gedcomList[1]
            print("<--" + level + "|" + tagData + "|" + "Y" + "|" + id)
        else:
            tagData = gedcomList[1]
            print("<--" + level + "|" + tagData + "|" + "N" + "|" + " ".join(gedcomList[2:]))