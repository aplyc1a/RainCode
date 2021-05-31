# RainCode

面向自然人的社工字典生成

## 介绍

口令用来鉴权，安全性要求我们要将口令设置的足够复杂且不混用，使得在枚举爆破时攻击者花费的时间代价是不可承受的，然而，现实与理想条件下是截然不同的，围绕人这一因素，弱口令的出现无法避免。

绝大多数的密码都带有人的属性，尽可能的获得更多的信息，将尽可能的匹配到正确的密码。社工字典的精髓在于：**密码编排模式**+**信息量**，这也是这个小工具的核心思想。

社工自然人信息收集：https://github.com/aplyc1a/blogs/blob/master/%E7%A4%BE%E5%B7%A5%E4%B8%AD%E7%9A%84%E8%87%AA%E7%84%B6%E4%BA%BA%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86.md

社工字典工厂：https://github.com/aplyc1a/toolkits/tree/master/0x00.%E5%AD%97%E5%85%B8%E6%96%87%E4%BB%B6/%E5%AD%97%E5%85%B8%E5%B7%A5%E5%8E%82

## 组成

**db**：存储弱口令文件。

**factory**：存储可用于提取模型文件的原材料。这部分源于https://github.com/aplyc1a/toolkits/tree/master/0x00.%E5%AD%97%E5%85%B8%E6%96%87%E4%BB%B6/%E5%AD%97%E5%85%B8%E5%B7%A5%E5%8E%82

**model**：存储用于生成字典的核心模型文件。model目录下预置了两个可用模型：

```text
big.model(全量模型)
smart.model(经典模型)
```

**config.json**：配置文件，需要使用前填入收集到的目标的个人信息。不知道的可以留空或删除。

**raincode.py**：程序主文件。

## 帮助

```text
python3 raincode.py -h
【必选参数】
-j/--json	加载配置文件
-m/--model	加载模板文件

【可选参数】
-h/--help        帮助
-o/--output      输出文件名。（缺省时标准输出）
#-e/--evolving    fuzz模式。对部分字符做变异操作。
-i/--import      导入通用弱口令。默认导入通用高频密码（db/common.txt）
```



## 使用

raincode通过读取模式文件（*.model）及社工信息配置文件（config.json）来生成定制化字典。

默认情况下已集成了一个用户通用密码模式文件"model/big.model"，该文件是从公开数据源中提取分析得来的。



**step1**：自然人信息收集，填入config.json。

**step2**：确认模型文件。也可以自行定义。*.model

**step3**：执行之。

```shell
python3 raincode.py -j config.json -m model/big.model -i 
```

![raincode](https://github.com/aplyc1a/RainCode/blob/master/2021-05-29_155836.png)