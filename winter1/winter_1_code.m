%Reading image
Image = imread('baboon.jpg');

%Displaying image
figure(1)
imshow(Image)
title('Original Image');


%Rotating  it
rotImage = imrotate(Image,90);
figure(2)
imagesc(rotImage)
title('Image rotated by $90^{\circ}$','Interpreter','latex')
imwrite(rotImage,'images/rotated90.png');

rotImage = imrotate(Image,45);
figure(3)
imshow(rotImage)
title('Image rotated by $45^{\circ}$','Interpreter','latex')
imwrite(rotImage,'images/rotated45.png');

%Translating Image
transImage =  imtranslate(Image,[100,100]);
figure(4)
imshow(transImage)
title('Translated Image');
imwrite(transImage,'images/translated.png');

%Cropping an Image
croppedImage = imcrop(Image,[50 30 400 600]);
figure(5)
imshow(croppedImage)
title('Cropped Image');
imwrite(croppedImage,'images/cropped.png');

%Warping an image
theta = 10;
tform = projective2d([cosd(theta) -sind(theta) 0.001; sind(theta) cosd(theta) 0.001; 0 0 1]);
warpedImage = imwarp(Image,tform);
figure(6)
imshow(warpedImage)
title('Warped Image');
imwrite(warpedImage,'images/warped.png');

%Thresholding an Image
threshImage = im2bw(Image, 0.5);
figure(7)
imshow(threshImage)
title('Thresholded Image');
imwrite(threshImage,'images/thresholded.png');

level = graythresh(Image);
threshImagebetter = im2bw(Image, level);
figure(8)
imshow(threshImagebetter);
title('Better thresholded image');
imwrite(threshImagebetter,'images/thresholded_better.png')

k = waitforbuttonpress

close all
