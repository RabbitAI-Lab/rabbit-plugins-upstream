# lan-knowledge-share

一键将本地文件目录部署为局域网可访问的 Web 知识库，开启 HTTP 服务实现局域网内知识共享。

- 任意目录即知识库：Markdown / Excel/CSV 表格 / HTML 报告 / 图片 / 音视频混合内容开箱即用
- 动态侧边栏、自动目录页、图片画廊（键盘切换）、表格在线预览、HTML 报告就地查看、全站全文搜索
- 目录增删改实时生效，刷新即更新，无需建库、无需预生成配置
- 零第三方依赖（仅需 Node.js 12+）

## 目录结构

```
lan-knowledge-share/
├── SKILL.md                 # 技能定义（触发说明与使用流程）
├── scripts/
│   └── deploy.js            # 一键部署入口（node deploy.js <目录> [选项]）
├── assets/
│   └── runtime/             # 内置前端运行时（index.html 模板 + assets）
└── references/
    └── skillhub-listing.md  # SkillHub 网页发布表单填写模板
```

## 快速开始

```
node scripts/deploy.js "<要分享的目录>" -n "站名" -p 8089
```

启动后按终端提示把局域网地址（http://<IP>:<端口>）发给同事即可访问。`node scripts/deploy.js --help` 查看全部选项。

## 部署形态

- **纯内容目录**（根目录无 index.html）：运行时注入，内容目录不落站点文件；无 README 时自动生成默认首页
- **自包含知识库**（已有 index.html+assets）：按原站点逻辑托管

## 发布到 SkillHub

1. 安装 CLI：`curl -fsSL https://skillhub.cn/install/install.sh | bash`（Windows 用户见官网安装指引）
2. `skillhub login` 完成登录与实名认证
3. `skillhub init --name lan-knowledge-share --category 知识管理`（或直接在官网网页发布）
4. `skillhub push` 上传文件，`skillhub publish` 提交审核

网页发布可参考 `references/skillhub-listing.md` 的表单文案。
