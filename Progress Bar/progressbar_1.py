from progress.bar import Bar
bar = Bar('Processing', max =  20)
a = 1
for i in range(20):
    a = 0
    bar.next()
bar.finish()
