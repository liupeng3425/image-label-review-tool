## 图片标注检查工具
这个工具是用来检查数据集的标签的。你可能需要重新配置图片的目录和`label.views.getLabel()`函数来适应你的具体需求。

#### 使用方法
你可能需要稍微学习一下Django的用法才能开始部署。部署完成后你可以找一些小伙伴帮你一起标注。

在标注过程中可以按键盘方便标注，默认行为：

* `←`：正确
* `→`：错误
* `↓`：不确定



**注意**⚠️

**没有用数据库保存标注进度，所以一关程序所有进度都会丢失！！！**（欢迎感兴趣的同学实现以后提PR）

部署完成以后：
* 访问 host:port/ 开始图片标注
* 访问 host:port/statistics/ 主动生成检查结果的统计

## Image Label Review Tool
This tool is implemented to review image labels of dataset based on Django.
You may need to reconfigure the data folder and `label.views.getLabel()`.

#### Usage
You may need to learn a little about Django usage to get started. You can collaborate with your partner with a web browser after deployment finished.

You can use keyboard shortcuts when you reviewing, default keymap:

* `←`：right
* `→`：wrong
* `↓`：unknown



**Caution**⚠️

**All review progress stored in RAM, so if you close backend program, all progress will lost!!!**

Welcome your pull request if you implement Database to store review progress.


Start label reviewing:
* http://host:port/ start reviewing
* http://host:port/statistics/ manually export reviewing results

#### LICENSE
Copyright 2019 liupeng3425

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.