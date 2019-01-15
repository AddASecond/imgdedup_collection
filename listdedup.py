import os,shutil

if __name__ == '__main__':
    if os.access("_duplicates",os.F_OK) == False:
        os.mkdir("_duplicates")
    listpath = "/home/chenqu/Projects/imageDeduplicate/duplicates.txt"
    cluster_num = 0
    flag = 0
    if os.access("_duplicates/"+ str(cluster_num),os.F_OK) == False:
        os.mkdir("_duplicates/"+ str(cluster_num))
    with open(listpath, 'r') as f:
        for line in f.readlines():
            if line != "" and line != "\n":
                img_name = line.split("/")[-1]
                print(img_name)
                if flag == 0:
                    print ("_duplicates/"+ str(cluster_num) + "/"+ img_name)
                    shutil.copyfile(line.split("\n")[0],"_duplicates/"+ str(cluster_num) + "/"+ img_name)
                else:
                    shutil.move(line.split("\n")[0],"_duplicates/"+ str(cluster_num) + "/"+ img_name)
                flag = flag + 1
            else:
                cluster_num = cluster_num + 1
                flag = 0
                if os.access("_duplicates/" + str(cluster_num), os.F_OK) == False:
                    os.mkdir("_duplicates/"+ str(cluster_num)) 
        
