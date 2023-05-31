from torch.utils.tensorboard import SummaryWriter
from get_map import global_get_map
import os

log_dir = "logs"
map_dir = os.path.join(log_dir,'map')
writer     = SummaryWriter(map_dir)

for epoch in range(10):
    model_path = os.path.join(log_dir, 'ep%03d_new.pth' % (5*(epoch + 1)))
    mAP = global_get_map(model_path_input=model_path,mode=0,epoch=epoch+1)
    writer.add_scalar('mAP', mAP, 5*(epoch + 1))