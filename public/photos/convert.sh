for i in *.jpeg
	# do convert "$i" -geometry 1080x1920^ -gravity center -crop 1080x1920+0+0 wallpaper/portrait-"$i"
	do convert "$i"  -resize 25% -quality 85% medium/"$i"
done
