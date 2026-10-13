fps = 30
frame_id = 95
video_nomi = "test.mp4"
vaqt = frame_id / fps
print("Video:", video_nomi)
print("vaqt (soniya):", vaqt)

print(f"{video_nomi} faylida {frame_id}-frame {vaqt:.f1} soniyaga togri keladi")
def frame_vaqti(frame_id, fps):
    return frame_id/fps
print(frame_vaqti(95, 30))
print(frame_vaqti(30,50))
