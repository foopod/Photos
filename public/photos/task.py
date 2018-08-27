import os, datetime

for file in os.listdir("."):
    if file.endswith(".jpeg"):
        date = datetime.datetime.fromtimestamp(int(os.path.getmtime(os.path.join(".", file)))).strftime('%Y-%m-%d');
        print(date)
        contents = "---\n" + "layout: post\n" + "title: " + file[:-5].title()+"\n" + "image: /public/photos/medium/"+ file+ "\n"+ "image-thumb: /public/photos/thumb/"+ file[:-5]+".jpg"+ "\n" + "caption: \n" + "date: " + date +"\n" +  "tags: []\n" + "---";
        f = open(os.path.join("../../_posts", date + "-" + file[:-5] + ".md") ,'w')
        f.write(contents)
        f.close()