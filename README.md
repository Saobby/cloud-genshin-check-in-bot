# cloud-genshin-check-in-bot
 云原神自动签到机,可部署在vercel

- - - - -

# 使用方法
## 1.获取Cookie
1. 去[这里](https://ys.mihoyo.com/cloud/#/)登录你的账户
2. 打开你的浏览器的开发者工具  
它通常能在浏览器右上角的菜单里找到:  
![](https://gp0.saobby.com/i/wQsxsFjMilQXe0P8.PNG)  
或者你可以直接按`F12`打开开发者工具
3. 点开发者工具(DevTools)顶部的`控制台`(`Console`)选项卡
4. 在那里输入`console.log(document.cookie)`，然后按回车
5. 现在你应该能看到下面出现了一堆字母，那是你的Cookie，把它保存好备用(你可以把它复制粘贴到一个记事本里)，**Cookie和你的账户密码一样重要，不要把它泄露给任何人**
## 2.部署
1. Fork这个仓库
2. 去[这里](https://vercel.com/login)登录或注册你的Vercel账户
3. 你现在应该跳转到了Vercel控制面板(Dashboard)，你应该能看见页面的右上角有一个大大的黑色按钮`新建...`(`Add New...`)，点击它，在弹出的下拉菜单中选择`项目`(`Project`)
4. `导入`(`Import`)刚刚你Fork出来的仓库
5. 点`环境变量`(`Environment Variables`)下拉菜单
6. `键`(`Key`)那里填上`mihoyo_cookies`，`值(会被加密)`(`Value (Will Be Encrypted)`)那里填上你在第一步得到的Cookie，点`添加`(`Add`)
7. 点黑色的`部署`(`Deploy`)按钮

