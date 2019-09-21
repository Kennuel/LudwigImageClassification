import Augmentor
l = Augmentor.Pipeline("./like_orig/")
d = Augmentor.Pipeline("./dislike_orig/")

l.rotate(probability=0.3, max_left_rotation=25, max_right_rotation=25)
l.zoom(probability=0.3, min_factor=0.9, max_factor=1.2)
l.random_distortion(probability=0.3, grid_width=4, grid_height=4, magnitude=8)
l.flip_left_right(probability=0.25)
l.sample(3600)

d.rotate(probability=0.3, max_left_rotation=25, max_right_rotation=25)
d.zoom(probability=0.3, min_factor=0.9, max_factor=1.2)
d.random_distortion(probability=0.3, grid_width=4, grid_height=4, magnitude=8)
d.flip_left_right(probability=0.25)
d.sample(3600)