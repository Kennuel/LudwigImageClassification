import Augmentor
l = Augmentor.Pipeline("./like_orig/")
d = Augmentor.Pipeline("./dislike_orig/")

l.rotate(probability=0.7, max_left_rotation=25, max_right_rotation=25)
l.zoom(probability=0.5, min_factor=1.1, max_factor=1.75)
l.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=8)
l.flip_left_right(probability=0.5)
l.flip_top_bottom(probability=0.5)
l.sample(3657)

d.rotate(probability=0.7, max_left_rotation=25, max_right_rotation=25)
d.zoom(probability=0.5, min_factor=1.1, max_factor=1.75)
d.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=8)
d.flip_left_right(probability=0.5)
d.flip_top_bottom(probability=0.5)
# d.sample(4908)