clc
clear ;
close all;
% mkdir()
level1 =str2mat('dcgan','wgan','wgangp');
for l1=1:1
    for l2 = 1:21
        file = strcat('E:\GAN\ganimage\',level1(l1,:),'\g',sprintf('%02d',l2),'\' );
        file_path =  file;% 图像文件夹路径
        disp(file_path)
        write_file = strcat('E:\GAN\ganimage-rotate\',level1(l1,:),'\g',sprintf('%02d',l2),'\' );
%         mkdir(write_file);
        
        
        img_path_list = dir(strcat(file_path,'*.jpg'));%获取该文件夹中所有jpg格式的图像
        img_num = length(img_path_list);%获取图像总数量
        if img_num > 0 %有满足条件的图像
            for z = 1:img_num %逐一读取图像
                image_name = img_path_list(z).name ;% 图像名
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
% file_path =  'C:\Users\Administrator\Desktop\ganimage\dcgan\';% 图像文件夹路径
% img_path_list = dir(strcat(file_path,'*.jpg'));%获取该文件夹中所有jpg格式的图像
% img_num = length(img_path_list);%获取图像总数量
% if img_num > 0 %有满足条件的图像
%     for z = 1:img_num %逐一读取图像
%         image_name = img_path_list(z).name ;% 图像名
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