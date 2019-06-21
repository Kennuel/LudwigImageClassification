import os
with open('ring_data.csv', 'w') as output_file:
    output_file.write('image_path,label\n')
    for name in ['like', 'dislike']:
        print('=== creating {} dataset ==='.format(name))
        path = '{}'.format(name)
        for file in os.listdir(path):
            if file.endswith(".jpg"):
                output_file.write('{},{}\n'.format(os.path.join(path, file), name))