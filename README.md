# Test Trials

### Changed
- requirements : versions deleted

### Commands
``` bash
# build image
$ docker build -t image-demo .

# build container
$ docker run --name app-demo -p 8000:8000 image-demo
```

### Publish
``` bash
# create toml file
$ fly launch
```