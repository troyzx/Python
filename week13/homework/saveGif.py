import imageio


def create_gif(image_list, gif_name):

    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.1)
    print("Complete !")
    return


def main(n):
    image_list = []
    for n in range(n):
        image_list.append('./fig/'+str(n) + '.png')
    gif_name = 'created_gif.gif'
    create_gif(image_list, gif_name)

if __name__ == "__main__":
    main()
