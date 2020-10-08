clc
clear;
close all;

% H:\20181203-Paper-EMDS5 Evaluation\20180717-EMDS5-All21\EMDS5-GTS
file_path =  'H:\Final-dataset-microbe-2019-04-29\EMDS5-GTM\';% ͼ���ļ���·��

img_path_list = dir(strcat(file_path,'*.png'));%��ȡ���ļ���������jpg��ʽ��ͼ��
img_num = length(img_path_list);%��ȡͼ��������
centroid=zeros(img_num,2);
if img_num > 0 %������������ͼ��
%     for z = 1:img_num %��һ��ȡͼ��
         for z = 1:img_num %��һ��ȡͼ��
        image_name = img_path_list(z).name ;% ͼ����
        fprintf('%d %s\n',z,strcat(file_path,image_name));% ��ʾ���ڴ����ͼ����
        %ͼ������� ʡ��
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
        ind = find(Ar ==max(Ar));%�ҵ������ͨ����ı��
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
inc = find(Aq ==max(Aq));%�ҵ������ͨ����ı��

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
%  imwrite(D,strcat('H:\��ɫ������boundingbox\',strcat(name,'-13.jpg')));
 imwrite(D,strcat(' H:\GTM-boundingbox\',strcat(name,'.jpg')));

    end
end