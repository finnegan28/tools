# tools
This is a simple tool that will read a file in as binary
Then using the specified blocksize it will compress that blocksize,
and then skip to the next block until it reaches the end of the file.

It will then find the compression ratio and the output will be saved in
a csv file. This can be plotted to a graph or excel sheet easily.

We currently use it to test an lz4 based compression algorithm as 
it allows us to monitor the rate that our randomly generated data
can be compressed. When we see a drop off in the compression rate
we know when to reseed.