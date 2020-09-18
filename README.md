# ImageProcessing
https://www.coursera.org/learn/image-processing/home/week/1

Week 1
- Human Visual System :  
    -   the cones that are very good at seeing at bright light and very, very concentrated around the fovea 
    -   and the rods which are spread all around the retina and are very good at seeing at very low light. 
    -   If we are in very low light conditions, we need the delta i, the change to be relatively high. 
    -   If we are in very high background light, we don't need so much change.
    -   Mach Bands : Perceived Intensity vs Actual Intensity 

- Reducing Image size to compress image for efficient storage and transmission purposes.
    -   Sampling : No. of total pixels, Spatial image domain
    -   Quantization  : No. of values picture can take / dpi
    
    
Week 3
- Enhance Image with poor lighting conditions to brightly illuminated lightning conditions
-   Reversible Transformations: Strictly Monotonically increasing/decresing func  - one to one mapping
-   Irreversible Transformations: Monotonically increasing/decresing func  - multiple values map to one
-   Histogram Equalization : Any Distribution to Uniform Distribution    
-       S = T(r) = (L-1) *Integral of P(r) from 0 to 1
-   Histogram Mapping :
        Map both images to uniform images, say fa and fb, 
            then take inverse of second mapping fb_inverse to first mapping fa, if multiple then take closet to first one.
        P(a) -> fa -> U(a)
        P(b) -> fb -> U(b)    
        P(a) -> P(b)
            fb'(f(a))
            Eg: f(a): 7  -> 10
                f(b): 15 -> 10
                so, 7 --> 15

-   Averaging pixels of neighbourhood : can cause bluring of edges
-   Averaging pixels of blocks which are very similar : removes noise without blurring images
-   Replace block by median : removes noise without blurring images, no new values are introduced like average, same pixel value as neighbour.
-   Second Derivative indicates sharp change in images. Like Jerk
-   Take second derivative (laplacian) of image and add to original to get clear image
-   Enhance Boundaries with Unsharp Mask : 
        - Blur Edges by taking avg of pixels in neibhbourhood
        - Subtract Original - Blur : Unsharp Mask
        - Add Unsharp Mask to Original Image : Result is enhanced boundaries

        
        

-                    
            



