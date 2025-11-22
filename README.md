# Mandelbrot and Julia Sets – Convergence Animation in Python

This project generates and visualizes the **Mandelbrot** and **Julia** sets by iterating complex mappings on a 2D grid of points and studying their convergence behavior.

The code produces both static images and animated GIFs that show how the sets emerge as the number of iterations increases.

---

## 🔍 What the code does

The script performs the following steps:

### 1. Create 2D grids in the complex plane

- For the **Mandelbrot set**, it defines a grid of complex numbers \( c = x + i y \) over a rectangular region.
- For the **Julia set**, it defines a similar grid of complex numbers \( z_0 = x + i y \).

### 2. Mandelbrot set iteration and frames

For the Mandelbrot set, the code iterates:

\[
z_{n+1} = z_n^2 + c, \quad z_0 = 0
\]

At each iteration:

- Points with \(|z_n| > 2\) are considered to have escaped.
- A matrix `VM` stores, for each point, the iteration number at which it last satisfied the convergence condition.
- For every iteration, an image is saved in the directory:

```text
framesMandelbrot/frame_{n:03d}.png

These frames show how the convergence pattern of the Mandelbrot set evolves with the number of iterations.

### 3. Mandelbrot GIF

After generating all the frames, the script:

- Loads the PNG files from framesMandelbrot/.

- Combines them into an animated GIF

### 4. Julia set

The code follows the same process with the Julia set.

### 📁 Output structure

After running the script, you should obtain:

framesMandelbrot/
    frame_000.png
    frame_001.png
    ...
framesJulia/
    frame_000.png
    frame_001.png
    ...

animacionMandelbrot.gif
animacionJulia.gif

along with four matplotlib figure windows showing the final results.

### 🛠️ Requirements

- The script uses:
- Python 3
- numpy
- matplotlib
- imageio
- os (standard library)

You can install the required external packages with:

pip install numpy matplotlib imageio

### ▶️ How to run

Save the script as, for example:

mandelbrot_julia_convergence.py

and run:

python mandelbrot_julia_convergence.py

The script will:

1. Create the framesMandelbrot and framesJulia directories (if they do not exist).
2. Generate and save all intermediate frames.
3. Build the animated GIFs.
4. Show the final static plots in separate figure windows.

### 🎯 Purpose

This project was created as part of my Physics degree to:

- Practice numerical methods in the complex plane.
- Explore the convergence properties of Mandelbrot and Julia sets.
- Visualize how fractal structures emerge as the number of iterations increases.

::contentReference[oaicite:0]{index=0}
