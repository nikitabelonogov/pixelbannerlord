# Pixel Banner
Convert an image to the Mount&Blade II Bannerlord banner.
> It only works with really small images! Like 16x16.

## Examples
Convert ![space_invader.png](examples/sources/space_invader.png?raw=true "Space invader") into this:

![space_invader.png](examples/results/space_invader.png?raw=true "Space invader")

Convert ![some_italian_plumber.png](examples/sources/some_italian_plumber.png?raw=true "Some Italian plumber") into this:

![some_italian_plumber.png](examples/results/some_italian_plumber.png?raw=true "Some Italian plumber")

## Install packages from requirements.txt
```shell script
pip install -r requirements.txt
```

## Usage
* Clone the repository
* Install packages from *requirements.txt*
    ```shell script
    pip install -r requirements.txt
    ```
* Run *main.py*
    ```shell script
    ./main.py ./examples/sources/space_invader.png
    ```
* Copy the output
* *Optional.* Go to [bannerlord.party](https://bannerlord.party/) and check the look of the banner
* Press Ctrl+V in the Banner Editor
    > Note that pasting with Ctrl+V will crash your game if you paste something that isn't a valid banner code.
