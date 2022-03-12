function alpha_trim_filter(input_filename)
    % Fliters the input image using Alpha-Trimmed Mean filter
    % Writes to disk.
    img = imread("images/" + input_filename + ".bmp");
    alpha_trim = zeros(size(img),"uint8");
    
    window_size = 3;
%     alpha = window_size^2*0.4;
    alpha = 4; % for window size of 3; ignoring 2 valeus on both sides
    offset = floor(window_size/2);
    alpha_trim(1:offset, :) = img(1:offset, :);
    alpha_trim(size(img,1)-offset-1:size(img,1), :) = img(size(img,1)-offset-1:size(img,1), :);
    
    alpha_trim(:, 1:offset) = img(:, 1:offset);
    alpha_trim(:, size(img,2)-offset-1:size(img,2)) = img(:, size(img,2)-offset-1:size(img,2));
    
    for i=offset+1 : size(img,1)-offset
        for j=offset+1 : size(img,2)-offset
            x = img(i-offset:i+offset, j-offset:j+offset);
            x = sort(x(:));
             alpha_trim(i,j) = mean(x(alpha/2 : length(x) - alpha));
        end
    end
    imwrite(alpha_trim,"images/" + input_filename + "_ATF.png")
    imwrite(img, "images/" + input_filename + ".png")
end