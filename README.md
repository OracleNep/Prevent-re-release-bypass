# Prevent-re-release-bypass

绕过某云WAF防重放检查的脚本

原理是利用py代码实现了网站给请求包加时间戳签名的过程，填入token和hex值便可通过此脚本计算出sign参数值，再将sign值填入请求包内发送即可伪造签名绕过某云的防重放检查

token值抓包获取，hex使用F12在网站前端获取
