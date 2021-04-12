im = getTitle();

run("Conversions...", "scale");

run("32-bit");

// Get min_value and max_value from stack
run("Z Project...", "projection=[Min Intensity]");
run("Select All");
getStatistics(area,mean,min_value,max);
close();
selectWindow( im );
run("Z Project...", "projection=[Max Intensity]");
run("Select All");	
getStatistics(area,mean_value,min);
close();

// rescale, log transform and background subtract the 
// image
selectWindow( im );
min_value = min_value + 0.00001; //log of zero diverges
run("Subtract...", "value=" +min_value+" stack");
norm_value = mean_value - min_value
run("Divide...", "value=" +norm_value+" stack");
run("Log", "stack");
run("Multiply...", "value=-1 stack");
run("Subtract Background...", "rolling=25 stack");
run("Gaussian Blur...", "sigma=2 stack");

// rescale for conversion without scale option
// Get min_value_2 and max_value
run("Z Project...", "projection=[Min Intensity]");
run("Select All");
getStatistics(area,mean,min_value_2,max);
close();
selectWindow( im );
run("Z Project...", "projection=[Max Intensity]");
run("Select All");	
getStatistics(area,mean,min,max_value);
close();

selectWindow( im );
run("Subtract...", "value=" +min_value_2+" stack");
norm_value_2 = max_value - min_value_2
run("Divide...", "value=" +norm_value_2+" stack");
run("Multiply...", "value=65530 stack");


run("Conversions...", " "); //disable scaling when converting from 32-bit to 16-bit

//run("Divide...", "value=2 stack");//to prevent saturation when later converting to 16-bit
run("16-bit")
  