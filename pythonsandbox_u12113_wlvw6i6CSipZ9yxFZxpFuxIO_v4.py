# The answer to this challenge is by using the ...
# ... filename_prefix="" with the f-string interpolation
# ... by adding +1 to the index value followed by a space
# ... the file name becomes: 1 Kingdom Hearts...
YouTube(playlist[i]).streams.filter(subtype="mp4").first()
.download(
  output_path=downloads_dir, 
  filename_prefix=f"{i+1} "
)
 

