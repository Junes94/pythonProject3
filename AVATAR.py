import function.csvload as acl
import function.calculate_basic as ccb


givenpath = 'C:/Users/MyPC/Desktop/실험실/2.실험데이터/AVATAR-SDSBD/post/22.09.13.DataSet_SI1기준/'
pathrest = 'Control/'
filename = '01.mp4.txt'

data = acl.load(pathrest, filename, givenpath)
joint = 'head'
xyz = ('x', 'y')

ccb.cal_vel(data, joint, xyz)
ccb.cal_accel(data, joint, xyz)
