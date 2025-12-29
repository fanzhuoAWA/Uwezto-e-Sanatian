演示地址：[乌斯托什语词典](https://sanatian.fanzhuo.xyz/)

[博客](https://blog.fanzhuo.xyz/blog/%E4%B8%BA%E4%BD%A0%E7%9A%84%E4%BA%BA%E9%80%A0%E8%AF%AD%E8%A8%80%E6%90%AD%E5%BB%BA%E5%9C%A8%E7%BA%BF%E8%AF%8D%E5%85%B8) 内阅读更佳

# 前言

人造语言（Constructed Language，简称Conlang）是指那些语音、语法和词汇都由创造者有意识设计的语言。与自然语言（如汉语、英语等）不同，人造语言并不随人类文化的演变而变化，而是根据特定的需求和目的进行构造。

你可以使用这个项目为你的人造语言搭建词典。

# 搭建

### 事前准备

在电脑上安装 git 、python 。

### 本地部署

点击 Fork ，创建新分支到你的仓库。

然后将仓库克隆到本地（在本地新建文件夹，右键运行 git 终端），在终端里输入 `git clone <你的仓库URL>` ，推荐使用SSH，可以不用魔法来推送更改。

至此，你成功在本地部署了 sanatian 。

### 改写词库

打开 `dictionary.txt` ，你将会看到原来的词库内容，你可以直接 <Kbd>Ctrl</Kbd> + <Kbd>A</Kbd> 全选后 <Kbd>backspace</Kbd> 删除掉。

你可以添加你的词库内容了！

运行自动添加程序：终端输入 `python add_word.py` ，简单易懂，跟着提示来就行了。

![](https://image.fanzhuo.xyz/file/AgACAgUAAyEGAASKws10AAOiaVKI7ad92S--cykte2j0ZD7yl7MAAggOaxuqx5FWNQOiBVye6BkBAAMCAAN5AAM2BA.png)

### 个性化修改

#### 按首字母筛选

默认的首字母筛选的字母为 `'A', 'B', 'C', 'D', 'Ð', 'E', 'É', 'Ë', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ñ', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'ß', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'` ，如果你想修改为自己的字母，可以打开 `dictionary.html` ，找到第 305 行附近的这个代码：

```javascript

const alphabetOrder = [
    'A', 'B', 'C', 'D', 'Ð', 'E', 'É', 'Ë', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'Ł', 'M', 'N', 'Ñ', 'O', 'Ö', 'P', 'Q', 'R', 'S',
    'ß', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
];

```

将里面的内容修改为你的字母。

#### 词性

如果你想使用自己的词性缩写或者新的词性，找到 60 行附件的这些代码：

```html

<h3 style="margin-bottom: 15px; color: #2c3e50; margin-top: 25px;">按类别筛选</h3>
<div class="category-filter" id="categoryFilter">
    <button class="category-btn active" data-category="all">全部词汇</button>
    <button class="category-btn" data-category="noun">名词 (n.)</button>
    <button class="category-btn" data-category="verb">动词 (v.)</button>
    <button class="category-btn" data-category="adj">形容词 (adj.)</button>
    <button class="category-btn" data-category="adv">副词 (adv.)</button>
    <button class="category-btn" data-category="pron">代词 (pron.)</button>
    <button class="category-btn" data-category="conj">连词 (conj.)</button>
    <button class="category-btn" data-category="int">感叹词 (int.)</button>
    <button class="category-btn" data-category="prep">介词 (prep.)</button>
    <button class="category-btn" data-category="art">冠词 (art.)</button>
    <button class="category-btn" data-category="det">限定词 (det.)</button>
    <button class="category-btn" data-category="num">数词 (num.)</button>
    </div>
</div>

```

修改它！（记得词库里的词性要和这个对应上）

### 本地预览，然后发布到 Github

终端输入 `python -m http.server` ，然后浏览器进入 `http://localhost:8000/dictionary.html` 查看效果，确认可以了，没有问题了，进行发布环节。

首先，你需要让 Git 知道你是谁，终端输入 `git config --global user.name "你的 Github 用户名"` 和 `git config --global user.email "你的 Github 使用的邮箱"` 。

然后，更改远程仓库为ssh*（如果是通过ssh克隆的不用改），输入 `git remote set-url origin git@github.com:xxx/xxx` 。

提交所有文件 `git add .` 。

发布本地提交 `git commit -m "项目初始化"` 。

将本地更改提交到远程仓库 `git push` 。

## 部署

打开 [Vercel](https://vercel.com/) ，点击右上角的 `Add New...` ，选择连接 Git 存储库，连接你的 Github （具体网上有教程）。

部署好后给你的项目添加域名，或者也可以使用 vercel 分配给你的 `.vercel.app` 域名，不过国内经常被墙。

## Q&A

Q1：人造语言吧里不是已经有一个词典软件了吗，相比之下 sanatian 有什么优点？

A1：人造语言吧里的那个软件只支持安卓，且离线，数据（词库）无法共享（其实可以把数据库发到其他设备，但是有点麻烦）， sanatian 则是一个网站，可以用任意连了网的设备打开，查询。

Q2：缺点呢？

A2：那个软件下载安装了直接就能用， sanatian 搭建相比之下比较麻烦。

## TODO

1、支持 `SQLite` 数据库格式。

如果你有什么改进意见，欢迎提交Issues。