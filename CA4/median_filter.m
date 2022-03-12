function median_filter(input_filename)

    img = imread("images/" + input_filename + ".bmp");

    med_filtred = zeros(size(img),"uint8");
    window_size = 3;
    offset = floor(window_size/2);
    med_filtred(1:offset, :) = img(1:offset, :);
    med_filtred(size(img,1)-offset-1:size(img,1), :) = img(size(img,1)-offset-1:size(img,1), :);
    
    med_filtred(:, 1:offset) = img(:, 1:offset);
    med_filtred(:, size(img,2)-offset-1:size(img,2)) = img(:, size(img,2)-offset-1:size(img,2));
    
    for i=offset+1 : size(img,1)-offset
        for j=offset+1 : size(img,2)-offset
             med_filtred(i,j) = median(img(i-offset:i+offset, j-offset:j+offset),"all");
        end
    end
    imwrite(med_filtred, "images/" + input_filename + "_MEDFILT.png")


end