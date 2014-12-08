# destroy.jpeg

Use JPEG to corrupt an image beyond recognition. Works through opening and saving an image with different quality values.

## Requires

* [Python](https://www.python.org/)
* [Pillow](https://pypi.python.org/pypi/Pillow)

## `destroyJPEG`

```python
destroyJPEG(minCompression, maxCompression, pathToFile, timesToIterate)
```

* **`minCompression`** - The lower quality value. The least possible value is 1.
* **`maxCompression`** - The higher quality value. The greatest possible value is 95.
* **`pathToFile`** - Path to image file.
* **`timesToIterate`** - Can be a single integer, or a list of integers. Saves image this many times (the more times, the least recognizable). If it is a list of integers, it will save a duplicate at each time in the list.

### Example

```python
destroyJPEG(1, 95, 'image.png', 20)
```
Saves an image called `image.d.jpg`.

```python
destroyJPEG(1, 95, 'image.png', [20, 40, 60])
```
Saves images `image.d.jpg`, `image.d20.png`, `image.d40.png`, and `image.d60.png` (`image.d.jpg` and `image.d60.png` are graphically equivalent).

### Command line

```
python destoyjpeg.py 1 95 image.png 20
```

```
python destroyjpeg.py 1 95 image.png 20 40 60
```