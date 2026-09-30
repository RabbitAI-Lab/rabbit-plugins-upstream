# AstraFlow Desktop Sandbox 核心机制与速查

## 1. 架构原理

```
[ 本地浏览器 ]
      │  HTTPS / WSS (带安全随机密码)
      ▼
[ 星图网关 : 6080 ]
      │
[ 洛杉矶 us-ca 沙箱 (Ubuntu 22.04 LTS, 8C8G) ]
  ├── Xvfb (:99) 1920x1080 虚拟显示
  ├── XFCE 窗口管理器 + 桌面环境
  ├── x11vnc (严格监听 127.0.0.1:5900，强密码校验)
  ├── websockify (安全将本地 5900 转换为 6080 WebSocket)
  ├── 系统时区自动对齐 America/Los_Angeles
  ├── 看门狗定时杀 xfce4-screensaver 防黑屏锁死
  └── Google Chrome (可选拉起合规 http/https 目标页面)
```

## 2. 常见问题与排坑记录

1. **为什么不需要在本地安装 VNC 客户端？**
   沙箱对外暴露的 6080 端口走的是 noVNC Web 服务，通过现代浏览器访问即可直接获得全功能键鼠控制与剪贴板同步，无需本地打洞或安装额外客户端软件。
2. **时区与 IP 一致性**：
   沙箱系统默认是 `Etc/UTC`。脚本在创建阶段自动执行软链接修改 `/etc/localtime` 为 `America/Los_Angeles`（或所选地域对应的时区），并重启浏览器确保 JavaScript 的 `Intl.DateTimeFormat().resolvedOptions().timeZone` 与出口 IP 达到环境自洽。
3. **安全审计与端口防护**：
   `x11vnc` 进程不暴露到公网接口，绑定于 `127.0.0.1:5900`，并由随机高强度密码文件 (`~/.vnc/passwd`) 进行身份检验，有效防范非授权访问。
4. **生命周期与费用**：
   沙箱创建后按运行时长计费。测试完毕请务必运行 `python3 scripts/sandbox_ctl.py kill <ID>` 或 `--all` 停止计费。
