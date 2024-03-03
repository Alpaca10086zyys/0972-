# 0972- 数据可视化实验
南开大学通识选修课大数据可视化基础的一些实验及文档说明😋😋。

## 实验一
复现Same Stats, Different Graphs Generating Datasets with Varied Appearance and Identical Statistics through Simulated Annealing论文中的实验，这篇论文的原文也可以在仓库里找到。

代码的用法是下载SameStatsCode文件夹，清空results文件夹内的所有内容，然后用命令行运行Same_Stats.py

语法格式为
```
python Same_Stats.py run [Shape_Start] [Shape_end] <iters=100000> <decimals=2> <num_frames=100>
```
初始图象的csv信息存放于seed_datasets文件夹中，如果你需要自定义初始图像，请务必以格式`<name>.csv`命名，然后以`name`替代`Shape_Start`。

缺少的模块请自行安装。

本实验源码提供生成gif的代码文件，同样用命令行运行，但由于笔者太懒没有写解析命令行的功能，所以输入```python gen_gif.py```后需要换行输入
```
Shape_Start
Shape_end
iters
```
如此便会在文件夹下生成固定格式命名的gif，只需要看gif的名称便可以知道起始图象，目标图象和扰动次数，每一张图片的信息在results文件夹下自动生成。

本实验提交了笔者的一些尝试，另外关于保存图片张数和保留小数的内容也可以自己修改python代码完成实验~
