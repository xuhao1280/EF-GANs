clc
clear ;
close all;
% mkdir()
level1 =str2mat('dcgan','wgan','wgangp');
for l1=1:1
    for l2 = 1:21
        file = strcat('E:\GAN\ganimage\',level1(l1,:),'\g',sprintf('%02d',l2),'\' );
        file_path =  file;% ͼ���ļ���·��
        disp(file_path)
        write_file = strcat('E:\GAN\ganimage-rotate\',level1(l1,:),'\g',sprintf('%02d',l2),'\' );
%         mkdir(write_file);
        
        
        img_path_list = dir(strcat(file_path,'*.jpg'));%��ȡ���ļ���������jpg��ʽ��ͼ��
        img_num = length(img_path_list);%��ȡͼ��������
        if img_num > 0 %������������ͼ��
            for z = 1:img_num %��һ��ȡͼ��
                image_name = img_path_list(z).name ;% ͼ����
                if image_name(1:9) == 'epoch4000'
                
%                     fprintf('%s%s\n',file_path ,image_name)
                    
                image =  imread(strcat(file_path,image_name));
                address = strcat( write_file,image_name(1:length(image_name)-4),'.jpg');
                 imwrite(image,address);
                I =imrotate(image,90);
                address = strcat( write_file,image_name(1:length(image_name)-4),'-90','.jpg');
               disp(address);
                 imwrite(I,address);
                I =imrotate(image,180);
                address = strcat( write_file,image_name(1:length(image_name)-4),'-180','.jpg');

                disp(address);
                 imwrite(I,address);
                I =imrotate(image,270);
                address = strcat( write_file,image_name(1:length(image_name)-4),'-270','.jpg');
              disp(address);
               imwrite(I,address);
                
                
                end
            end
        end
        
    end
end
% file_path =  'C:\Users\Administrator\Desktop\ganimage\dcgan\';% ͼ���ļ���·��
% img_path_list = dir(strcat(file_path,'*.jpg'));%��ȡ���ļ���������jpg��ʽ��ͼ��
% img_num = length(img_path_list);%��ȡͼ��������
% if img_num > 0 %������������ͼ��
%     for z = 1:img_num %��һ��ȡͼ��
%         image_name = img_path_list(z).name ;% ͼ����
%         
%         image =  imread(strcat(file_path,image_name));
%         
%         I =imrotate(image,90);
%         address = strcat( file_path,image_name(1:length(image_name)-4),'-90','.jpg');
%         disp(address);
%         imwrite(I,address);
%         I =imrotate(image,180);
%         address = strcat( file_path,image_name(1:length(image_name)-4),'-180','.jpg');
%         disp(address);
%         imwrite(I,address);
%         I =imrotate(image,270);
%         address = strcat( file_path,image_name(1:length(image_name)-4),'-270','.jpg');
%         disp(address);
%         imwrite(I,address);
%         
%         
%         
%     end
% end