print("Video: a.mp4")
print("Video: b.avi")
def say_hello():
    print("salom")

say_hello()
say_hello()
say_hello()

def show_video(name):
    print("video:", name)

show_video("a.mp4")
show_video("b.avi")

def show_info(name, fps):
    print("Video:", name, "FPS:", fps)
show_info("a.mp4", 25)

def multiply(a,b):
    return  a * b
multiply(4,5)

videos = ["a.mp4", "b.avi", "c.mov"]
print(videos)
print(videos[0])
print(videos[1])
print(len(videos))
videos.append("d.mkv")
print(videos)
videos[0] = "new.mkv"

videos.remove("b.mkv")

print("c.mkn" in videos)
print("zzz.mp4" in videos)

videos = ["a.mp4", "b.mp4", "g.mp4"]
for v in videos
    print("video:", v)
for i, v in enumerate(videos)
    print(i,v)

def count_mp4(files):
    count = 0
    for f in files:
        if f.endswith(".mp4"):
            count = count + 1
    return  count
print(count_mp4(["a.mp4", "b.avi", "c.mp4"]))