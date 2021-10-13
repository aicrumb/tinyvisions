# TinyVisions

by [crumb](https://twitter.com/aicrumb)



![](anavocadoarmchairanarmchairintheshapeofanavocado.png)

`an avocado armchair`

### Use

##### GPU:

```
git clone https://github.com/openai/CLIP && pip install -e ./CLIP
python tinyvisions.py "prompt" 2000
```

where 2000 is the iterations, and "prompt" is .. your prompt

##### CPU:

change line 11 from `d='cuda'` to `d='cpu'`, then use as instructed above



#### Notebook

(Don't use the notebook on colab's k80s. it's way too slow. please. for your own sanity, it's in there if you "want" to use it though)
  [![Open in Colab](https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://githubtocolab.com/aicrumb/tinyvisions/blob/master/tinyvisions.ipynbb)
