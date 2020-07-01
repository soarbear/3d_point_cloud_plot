import numpy as np
import mayavi.mlab

print(np.load('test_point_cloud.npy', encoding='latin1'))
print(np.load('test_point_cloud.npy', encoding='latin1').size)
print(np.load('test_point_cloud.npy', encoding='latin1').shape)
print(np.load('test_point_cloud.npy', encoding='latin1').ndim)

#z = np.fromfile(str("test_point_cloud.npy"), dtype=np.float32)
coef = 110.0 # Chage coefficient here for Z(depth).
z = np.load('test_point_cloud.npy', encoding='latin1').reshape([-1]) * coef
print(f'z.shape:{z.shape}\nz[]: {z}')

x = np.linspace(0,415,416)
y = np.linspace(0,0,416)
for i in range(1,128):
  x_temp = np.linspace(0,415,416)
  y_temp = np.linspace(i,i,416)
  x = np.append(x, x_temp)
  y = np.append(y, y_temp)

print(f'x.shape: {x.shape} x.size: {x.size}\ny.shape: {y.shape} y.size: {y.size}\nz.shape: {z.shape} z.size: {z.size}')
col = z
fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(416*5,128*5))
mayavi.mlab.points3d(x, y, z,
                     col,# Values used for Color
                     mode="point",
                     colormap='spectral',# 'bone', 'copper', 'gnuplot'
                     #color=(0, 1, 0),# Used a fixed (r,g,b) instead
                     figure=fig,
                     )

x=np.linspace(5,5,50)
y=np.linspace(0,0,50)
z=np.linspace(0,5,50)
mayavi.mlab.plot3d(x,y,z)
mayavi.mlab.show()
