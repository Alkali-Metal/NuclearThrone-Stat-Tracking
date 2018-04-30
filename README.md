# Nuclear Throne Statistic Tracking

Keep in mind that this software is relatively incomplete, it currently can ONLY live update data and store the finished runs in JSON. Nothing else.

## Installing

Ensure that you have the following installed:
 - Python 3
 - Nuclear Throne

Fill in the proper settings in the `config.template.py` and then rename it to `config.py`. Run `main.py` through a command prompt.

</br>
</br>

## FAQ:

> The program isn't logging my current run to the JSON file and I have `live_logging` enabled in the config?!

Just wait, the program only actually logs the data to the permanent files when the run has 100% finished. Meaning that if you've only done one run while the program is running and that's it, it won't be logging anything to the file.

</br>

> What does `live_logging` do in the config if it doesn't make the files update live?

It updates the text files in the `stats/` directory so that you can have something like OBS read them and then create a stream overlay or something.

</br>

> Why isn't `X` working?

Are you on Windows or Mac? If yes, have fun. I don't support Windows to any degree. If you want support from me, you'll need to be running a Linux distrobution (and even then, I may not support it depending on my familiarity with the distro).

</br>

> Why don't you support Mac and Windows?

I don't like them. Though I do somewhat like Mac more than Windows, so you may get some help on Mac, but probably not as I don't have one so it is hard for me to test on it and figure stuff out. But Windows I can just about guarantee that you will get 0 support from me.

</br>
</br>

## Upcoming:
 - Local webpage to view statistics with nice graphs and all fun stuff to analyse your playing.
