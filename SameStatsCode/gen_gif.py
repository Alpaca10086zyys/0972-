
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.image import imread
from tqdm.rich import tqdm

start = input()
end = input()
iters = input()


bar=tqdm(total=100)
bar.set_description("Generating image list")
# 图片路径和格式
image_format = f"results/{start}-{end}/iters={iters}/"+"image-{num:05d}.png"

# 创建图像列表
image_list = []
for i in range(100):
    image_path = image_format.format(num=i)
    image = imread(image_path)
    image_list.append(image)
    bar.update(0.4)

# 创建子图
fig, ax = plt.subplots()

# 初始化图像对象
bar.set_description("initiating image object")
img = ax.imshow(image_list[0], animated=True)
bar.update(10)

# 更新函数，用于每一帧的图像更新
def update(frame):
    img.set_array(image_list[frame])

bar.set_description("generating gif")
# 创建动画
ani = FuncAnimation(fig, update, frames=len(image_list), interval=100)
bar.update(30)

bar.set_description("saving animation...")
# 保存为动画文件
ani.save(f'animation_{start}_to_{end}_{iters}.gif', writer='pillow')
bar.update(20)
bar.close()
print("finish!")