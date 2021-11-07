import pandas as pd


df=pd.read_csv("movies.csv")
df.columns
features=['keywords','cast','genres','director','original_title']
for feature in features:
    df[feature] = df[feature].fillna('')


def combine_features(row):
    try:
        return row['keywords']+" "+row['cast']+" "+row["genres"]+" "+row["director"]+" "+row['original_title']
    except:
        print ("Error:", row)

df["combined_features"] = df.apply(combine_features,axis=1)


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

cosine_sim = cosine_similarity(count_matrix)




def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


from tkinter import *
   
def show_data():
    txt.delete(0.0, 'end')
    movie =ent.get()
    movie_referred =movie        
    movie_index = get_index_from_title(movie_referred)
        
                
    i=int(movie_index)
    Similar_movies = list( enumerate(cosine_sim[i]))
                
    sorted_similar_movies = sorted(Similar_movies,key = lambda x:x[1], reverse = True)
                
                
    i=0;
    j=0;
    List =[None]*10
    for element in sorted_similar_movies:
            
            
            s=get_title_from_index(element[0])
            List[j]=s
            j=j+1;
            
    
            i=i+1;
            if i>=10:
                break
            
            
    for x in range(len(List) -1, -1, -1):
        t="\n"
        txt.insert(0.0, List[x])
        txt.insert(0.0, t)
           
       
   
root=Tk()
root.geometry("420x300")
               
l1 = Label(root, text="Enter Movie name: ")
l2 = Label(root, text="Top Ten Recomendation For You: ")
               
ent =Entry(root)
            
l1.grid(row=0)
l2.grid(row=2)
               
ent.grid(row=0, column=1)
               
                          
txt=Text(root,width=50,height=13, wrap=WORD)
txt.grid(row=3, columnspan=2, sticky=W)
               
btn=Button(root, text="Search", bg="red", fg="white", command=show_data)
btn.grid(row=1, columnspan=2)
root.mainloop()
    





   