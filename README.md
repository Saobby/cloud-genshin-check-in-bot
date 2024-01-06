# cloud-genshin-check-in-bot
 云原神自动签到机,可部署在vercel

*这个项目目前处于测试阶段*

- - - - -

# 使用方法
## 1.获取Cookie
1. 去[这里](https://ys.mihoyo.com/cloud/#/)登录你的账户，登录完之后**刷新页面**
2. 打开你的浏览器的开发者工具  
它通常能在浏览器右上角的菜单里找到:  
![](https://gp0.saobby.com/i/wQsxsFjMilQXe0P8.PNG)  
或者你可以直接按`F12`打开开发者工具
3. 点开发者工具(DevTools)顶部的`网络`(`Network`)选项卡，选择`Fetch/XHR`  
![image](https://github.com/Saobby/cloud-genshin-check-in-bot/assets/101960076/3261d43c-d7f4-4fed-8345-1289ae91aa00)  
4. 在下面找到`webLogin`，点击它，在`请求标头`(`Request Headers`)栏复制你的Cookie  
![image](https://github.com/Saobby/cloud-genshin-check-in-bot/assets/101960076/2ccf233b-1038-4b83-868a-84f389a9404a)  
5. 把复制下来的Cookie保存好备用(你可以把它复制粘贴到一个记事本里)，**Cookie和你的账户密码一样重要，不要把它泄露给任何人**
## 2.部署
1. Fork这个仓库
2. 去[这里](https://vercel.com/login)登录或注册你的Vercel账户
3. 你现在应该跳转到了Vercel控制面板(Dashboard)，你应该能看见页面的右上角有一个大大的黑色按钮`新建...`(`Add New...`)，点击它，在弹出的下拉菜单中选择`项目`(`Project`)
4. `导入`(`Import`)刚刚你Fork出来的仓库
5. 点`环境变量`(`Environment Variables`)下拉菜单
6. `键`(`Key`)那里填上`mihoyo_cookies`，`值(会被加密)`(`Value (Will Be Encrypted)`)那里填上你在第一步得到的Cookie **(注意末尾不要有换行)**，点`添加`(`Add`)
7. 点黑色的`部署`(`Deploy`)按钮
8. 等待Vercel完成部署，如果你看到`祝贺!`(`Congratulations!`)的字样，说明你已经部署成功了(不要关注下面的Not Found)，现在，你应该已经能够在每天早上的7点到8点自动签到
## 3.更新Cookie
1. 遗憾的是，Cookie并不是永久的，它有一定有效期，因此，你还需要定期更新Cookie(例如每周一次，对你来说应该不算难，毕竟你都有时间玩游戏)
2. (在一周之后)重新去[这里](https://ys.mihoyo.com/cloud/#/)登录你的账户，并重复`1.获取Cookie`中的步骤，得到一个新的Cookie
3. 打开[Vercel控制面板](https://vercel.com/dashboard)，点击你创建的签到机项目，点击顶部的`设置`(`Settings`)选项卡，点击侧边栏的`环境变量`(`Environment Variables`)
4. 拉到最底下，点击`mihoyo_cookies`环境变量右边的三个点，点`编辑`(`Edit`)
5. 把新的Cookie复制粘贴到`值`(`Value`)输入框里 **(注意末尾不要有换行)**，点右下角的`保存`(`Save`)
6. 点击顶部的`部署`(`Deployments`)选项卡，点击最上面那个部署右边的三个点，在弹出的菜单中选择`重新部署`(`Redeploy`)，点击弹窗中的`重新部署`(`Redeploy`)按钮，等待Vercel完成部署
7. 你现在已经成功更新了Cookie，记得一周后再来重复这个步骤

- - - - -

# Q&A
1. 为什么你不能自动更新Cookie  
因为获取Cookie需要登录，而登录有可能需要完成人机验证，这不是机器能独立完成的  
2. 它的原理是什么  
调用云原神的登录接口，就像你用浏览器登录一样  
3. 会封号吗  
应该不会吧，没这个必要。不过不排除这个可能，如果被封了，请自己负责，当然你也可以在Issue里告诉我  
4. 我看了你的代码，`combo_token`中的`sign`的计算方法是从哪里来的  
来自对云原神网页JS的逆向分析
