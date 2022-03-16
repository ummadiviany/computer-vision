function ssim = get_ssim(x,y)
    % Returns the SSIM val for a given image or local patch
    x = double(x);
    y = double(y);
    C = 0.0001;
    ux = mean(x,"all");
    sigx = std2(x);
    uy = mean(y,"all");
    sigy = std2(y);
    sigxy = sum((x-ux).*(y-uy),"all")/(numel(x)-1);
    ssim = (2*ux*uy*2*sigxy)/((ux^2 + uy^2)*(sigx^2 + sigy^2) + C);
end