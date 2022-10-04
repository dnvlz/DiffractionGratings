# DiffractionGratings

## First pattern
Our ability to resolve detail in astronomical observations is limited by the diffraction of light in our telescopes. Light from stars can be treated effectively as coming from a point source at infinity. When such light, with wavelength $\lambda$, passes through the circular aperture of a telescope (which we’ll assume to have unit radius) and is focused by the telescope in the focal
plane, it produces not a single dot, but a circular diffraction pattern consisting of central spot
surrounded by a series of concentric rings. The intensity of the light in this diffraction pattern
is given by
$$I(r) =\left(\frac{J_1(kr)}{kr}\right)^2,$$
where $r$ is the distance in the focal plane from the center of the diffraction pattern, $k =\frac{2\pi}{\lambda}$,
and $J_1(x)$ is a Bessel function. 

We wrote a program that makes a density plot of the intensity of the circular diffraction pattern of a point light source with $\lambda = 500 nm$, in a square region of the focal plane,
using the formula given above. The pictures covers values of $r$ from zero up to about $1\mu m$.

The central spot in the
diffraction pattern is so bright that it may be difficult to see the rings around it on the computer
screen. A simple way to deal with it is to find an appropriate color scheme for the density plot. For a more sophisticated solution to the problem, the imshow function has an additional argument vmax
that allows you to set the value that corresponds to the brightest point in the plot. For instance,
if you say “imshow(x,vmax=0.1)”, then elements in x with value 0.1, or any greater value, will
produce the brightest (most positive) color on the screen. By lowering the vmax value, you can
reduce the total range of values between the minimum and maximum brightness, and hence
increase the sensitivity of the plot, making subtle details visible. (There is also a vmin argument
that can be used to set the value that corresponds to the dimmest (most negative) color.) For
this exercise a value of vmax=0.01 appears to work well.

## Second pattern
We study a system where ight with wavelength $\lambda$ is incident on a diffraction grating of total width $w$, gets diffracted, is
focused with a lens of focal length $f$, and falls on a screen. Theory tells us that the intensity of the diffraction pattern on the screen, a distance $x$ from the
central axis of the system, is given by
$$I(x)=\int_{-w/2}^{w/2}\bigg|\sqrt{q(u)}e^{i2\pi x u/\lambda f}du \bigg|^2,$$
where $q(u)$ is the intensity transmission function of the diffraction grating at a distance $u$ from
the central axis, i.e., the fraction of the incident light that the grating lets through. We consider a grating with transmission function $q(u) = sin^2 \alpha u$ for a grating whose slits have separation $20 \mu m$. With this function, we calculate and graph the intensity of the diffraction pattern produced by the grating having ten slits in total, when the incident light has wavelength $\lambda = 500 nm$. We assume the lens has a focal length of 1 meter and the screen is 10 cm
wide. A visualization of how the diffraction pattern would look on the screen is shown.
