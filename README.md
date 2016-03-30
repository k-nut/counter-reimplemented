#Counter - reimplemented

A small reimplementation of Python's [Counter Class](https://docs.python.org/2/library/collections.html#collections.Counter)
feature that lets you increment values in a dictionary like object without having to check if they are there.

```
c = Counter()
c['foobar'] += 1 # Note: No KeyError here!
assert c['foobar'] == 1
```

## Setup
Install `py.test` (and `pytest-watch`) and run the test. Run `ptw .` to rereun the tets whenever a files changes
```
pip install -r requirements.txt
```

## Other
Originally presented at [Berlin Hack and Tell #43](http://www.meetup.com/Berlin-Hack-and-Tell/events/229872414/?)
