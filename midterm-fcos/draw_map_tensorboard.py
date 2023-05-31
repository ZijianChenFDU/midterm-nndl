from torch.utils.tensorboard import SummaryWriter
import numpy as np
import os

# ------------------------------------- #
#      绘制tensorboard格式的mAP曲线      #
# ------------------------------------- #

# ------------------------------------- #
#            请务必修改logdir            #
# ------------------------------------- #

logdir = ".\logs\loss_2023_05_28_02_26_50"
map_list = np.loadtxt(os.path.join(logdir,'epoch_map.txt'))
print(map_list)
writer     = SummaryWriter("map")
for epoch in range(10):
    print(map_list[epoch+1])
    writer.add_scalar('mAP', map_list[epoch+1], 5*(epoch+1))