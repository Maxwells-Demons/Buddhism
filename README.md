# 与佛论禅（base64加密版）

这其实是大一寒假无聊写的，现在才上传，实现原理也比较简单。最近是真的忙，一堆考试和作业，有时间再写详细介绍。

我当初为啥要写这东西，真是闲的蛋疼。

这个程序的GUI是用tkinter搭建的，没有用到任何布局，组件坐标完全是自己随手捏的。

它的功能也非常简单：在吾言处输入要加密的文字，点击听佛说宇宙的真谛，就能得到打码后的文字；将吾闻处输入要加密的文字，点击参悟佛所言的真意，就能得到解码后的文字。如果显示“太深奥了，参悟不出个中真意……”则说明给出的佛经有误。中间的普渡众生是功能说明。

而加密的原理则十分暴力，只是将输入的字符串用base64加密，将密文字符加上字符串中的下标偏移映射到佛学字典中。解密的时候就反过来操作。

最后，每当任何一个按键被按下（总共就只有3个吧），左上角都会刷新一句佛学谚语，陶冶情操。

运行图片：
![buddhism](/images/buddhism.png)
