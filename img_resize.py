from PIL import Image
image_path = 'C:/Users/iaren/TextRemoveNN/dataset'
for i in range(1, 33, 1):
    if i < 32:
        img = Image.open(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/dataset/0 ({i}).jpg')
        new_image = img.resize((256, 256))
        new_image.save(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/resz_data/0 ({i}).jpg')
    else:
        if i < 33:
            img = Image.open(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/dataset/0 ({i+1}).jpg')
            new_image = img.resize((256, 256))
            new_image.save(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/resz_data/0 ({i}).jpg')
        else:
            img = Image.open(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/dataset/0 ({i+2}).jpg')
            new_image = img.resize((256, 256))
            new_image.save(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/resz_data/0 ({i}).jpg')

