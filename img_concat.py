import sys
from PIL import Image
for i in range(1, 98, 1):
    if i < 32:
        images = [Image.open(x) for x in [f'C:/Users/iaren/PycharmProjects/TextRemoveNN/resz_data/0 ({i}).jpg',
                                      f'C:/Users/iaren/PycharmProjects/TextRemoveNN/resz_data/3 ({i}).jpg']]

    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    new_im.save(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/ultaa/0 ({i}).jpg')

# import cv2
# from PIL import Image
#
#
# for i in range(1, 98, 1):
#     img = cv2.imread(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/dataset/0 ({i}).jpg')
#     img3 = cv2.imread(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/dataset/3 ({i}).jpg')
#     im_h = cv2.hconcat([img, img3])
#     # cv2.imshow(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/1 ({i}).jpg', im_h)
#     im_h.save(f'C:/Users/iaren/PycharmProjects/TextRemoveNN/ultaa/0 ({i}).jpg')
