clc
clear;
close all;

% H:\20181203-Paper-EMDS5 Evaluation\20180717-EMDS5-All21\EMDS5-GTS
file_path =  'H:\Final-dataset-microbe-2019-04-29\EMDS5-GTM\';% 图像文件夹路径

img_path_list = dir(strcat(file_path,'*.png'));%获取该文件夹中所有jpg格式的图像
img_num = length(img_path_list);%获取图像总数量
centroid=zeros(img_num,2);
if img_num > 0 %有满足条件的图像
%     for z = 1:img_num %逐一读取图像
         for z = 1:img_num %逐一读取图像
        image_name = img_path_list(z).name ;% 图像名
        fprintf('%d %s\n',z,strcat(file_path,image_name));% 显示正在处理的图像名
        %图像处理过程 省略
        image =  imread(strcat(file_path,image_name));
%         image =  imread(strcat(file_path,'EMDS5-g08-01-GTS.png'));
if ndims(image)==3
    image= im2bw(image);
end
image=im2bw(image);
%           image= rgb2gray(image);
%  figure,imshow(image);
        L = bwlabel(image);
       
%            figure,imshow(L);
        
        stats = regionprops(L,'all');
        Ar = cat(1, stats.Area);
        ind = find(Ar ==max(Ar));%找到最大连通区域的标号
        angle = stats(ind).Orientation;
        B = imrotate(L,-angle);
%         figure;
%         imshow(B);
% %        B = bwlabel(B,8);
%         STATSS = regionprops(B,'all');

%         figure,imshow(B),rectangle('Position',STATSS(1).BoundingBox,'Curvature',[0,0],'LineWidth',2,'LineStyle','--','EdgeColor','r','FaceColor','r');
%      B=B(2:end-1,2:end-1);
statss = regionprops(B);
Aq = cat(1, statss.Area);
inc = find(Aq ==max(Aq));%找到最大连通区域的标号

%  figure;
%        imshow(B);
x1 =statss(inc).BoundingBox;
        x=uint16(x1);
      
% %        C=B(171:255,149:288);
%         C=B(x(2):x(2)+x(4)-2,x(1):x(1)+x(3)-2);
% %         figure;
% %         imshow(C);
%         imwrite(C,strcat('H:\GTM-boundingbox\',image_name));
% %         H:\20181203-Paper-EMDS5 Evaluation\20180717-EMDS5-All21\EMDS5-Original
name = image_name(1:12);
%  original_image =  imread(strcat('I:\20181203-Paper-EMDS5 Evaluation\20180717-EMDS5-All21\EMDS5-Original\',strcat(name,'.jpg')));
%  original_image =  imread(strcat('H:\save13\',strcat(name,'-13.jpg')));
 original_image =  imread(strcat('H:\Final-dataset-microbe-2019-04-29\EMDS5-Original\',strcat(name,'.png')));
 original_image = imrotate(original_image,-angle);
 D=original_image(x(2):x(2)+x(4)-2,x(1):x(1)+x(3)-2,:);
%  imwrite(D,strcat('H:\颜色抖动的boundingbox\',strcat(name,'-13.jpg')));
 imwrite(D,strcat(' H:\GTM-boundingbox\',strcat(name,'.jpg')));

    end
end