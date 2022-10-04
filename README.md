# DiffractionGratings

Our ability to resolve detail in astronomical observations is limited by the diffraction of light in our telescopes. Light from stars can be treated effectively as coming from a point source at infinity. When such light, with wavelength $\lambda$, passes through the circular aperture of a telescope (which we’ll assume to have unit radius) and is focused by the telescope in the focal
plane, it produces not a single dot, but a circular diffraction pattern consisting of central spot
surrounded by a series of concentric rings. The intensity of the light in this diffraction pattern
is given by
$$I(r) =\left(\frac{J_1(kr)}{kr}\right)^2,$$
where $r$ is the distance in the focal plane from the center of the diffraction pattern, $k =\frac{2\pi}{\lambda}$,
and $J_1(x)$ is a Bessel function. 

We show a program that makes a density plot of the intensity of the circular diffraction pattern of a point light source with $\lambda = 500 nm$, in a square region of the focal plane,
using the formula given above. The pictures covers values of $r$ from zero up to about $1\mu m$.

The central spot in the
diffraction pattern is so bright that it may be difficult to see the rings around it on the computer
screen. A simple way to deal with it is to find an appropriate color scheme for the density plot. Foa more sophisticated solution to the problem, the imshow function has an additional argument vmax
that allows you to set the value that corresponds to the brightest point in the plot. For instance,
if you say “imshow(x,vmax=0.1)”, then elements in x with value 0.1, or any greater value, will
produce the brightest (most positive) color on the screen. By lowering the vmax value, you can
reduce the total range of values between the minimum and maximum brightness, and hence
increase the sensitivity of the plot, making subtle details visible. (There is also a vmin argument
that can be used to set the value that corresponds to the dimmest (most negative) color.) For
this exercise a value of vmax=0.01 appears to work well.
