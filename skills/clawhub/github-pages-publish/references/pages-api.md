# GitHub Pages 参考：API、自动构建、故障排查

部署静态站点时按需查阅本文件。

## 关键 REST API 端点

| 操作 | 方法 & 路径 |
|------|-------------|
| 创建仓库 | `POST /user/repos`，body `{"name": "...", "private": false}` |
| 上传/更新单个文件 | `PUT /repos/{owner}/{repo}/contents/{path}`，body `{"message", "content"(base64), "branch"}` |
| 启用 Pages | `POST /repos/{owner}/{repo}/pages` |
| 查询 Pages 状态 | `GET /repos/{owner}/{repo}/pages`（`status` 字段：`built` 表示就绪） |
| 获取当前登录用户 | `GET /user`（用于解析 owner） |

上传单个文件要点（「往现有仓库追加页面」最轻量的方式，不依赖 git、不覆盖已有文件）：

- `content` 需 **base64 编码**。
- **新建文件**：直接 `PUT` 即可。
- **更新已有文件**：先 `GET /repos/{owner}/{repo}/contents/{path}` 取 `sha`，再 `PUT` 时带上该 `sha`，否则返回 422。
- 远程文件名用英文（如 `jiuzhaigou-vs-leshan.html`），避免中文被 URL 百分号编码。

启用 Pages 请求体（legacy 分支模式）：

```json
{
  "build_type": "legacy",
  "source": { "branch": "gh-pages", "path": "/" }
}
```

请求头（必需）：

```
Authorization: Bearer <token>
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2022-11-28
User-Agent: github-pages-publish
```

## 访问地址规则

| 仓库类型 | 仓库名 | 访问地址 | 发布分支 |
|----------|--------|----------|----------|
| 用户/组织主页 | `<owner>.github.io` | `https://<owner>.github.io` | `main` |
| 项目页 | 任意 `repo` | `https://<owner>.github.io/<repo>` | `gh-pages`（默认） |

一个账号只能有一个用户主页；项目页数量不限。

## 自定义域名

把默认的 `https://<owner>.github.io/<repo>` 换成自有域名（如 `example.com`）：

1. **仓库根放 `CNAME` 文件**（内容仅一行域名，不带协议）：
   ```
   example.com
   ```
   用 contents API 上传：`PUT /repos/{owner}/{repo}/contents/CNAME`，内容即域名那一行（发布源是 `gh-pages` 就放到该分支根）。
2. **DNS 解析**（在域名服务商处配置）：
   - 子域名（如 `www`）：加 `CNAME` 记录，主机 `www`，值 `<owner>.github.io`。
   - 裸域（`example.com` 不带 www）：加 `A` 记录指向 GitHub Pages 的 4 个 IP：`185.199.108.153`、`185.199.109.153`、`185.199.110.153`、`185.199.111.153`。
3. **启用 HTTPS**：仓库 Settings → Pages → Custom domain 填域名 → Save → 勾选 Enforce HTTPS（证书约几分钟自动签发）。

注意：`CNAME` 文件必须常驻仓库，否则自定义域名会失效；一次只能绑一个域名。

## 静态生成器自动构建（GitHub Actions）

若站点需要构建步骤（Hugo / Jekyll / Vite / Astro 等），把 Pages 源设为 `workflow`，并用 Actions 自动构建发布。

`POST /repos/{owner}/{repo}/pages` 改为：

```json
{ "build_type": "workflow" }
```

在仓库 `.github/workflows/pages.yml` 写入（以静态 HTML 为例，改用其他 action 可支持各类生成器）：

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

若站点有构建命令（Hugo、Vite、`npm run build` 等），在 `build` 任务的 `upload-pages-artifact` 之前插入构建步骤，并把 `path` 指向产物目录：

```yaml
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist   # 改成实际产物目录
```

## 故障排查

- **刚部署 404**：首次部署需 1–3 分钟；确认仓库为 public；确认 `index.html` 在发布分支根目录（而非子目录）。
- **`POST /pages` 返回 409**：Pages 可能已启用或正在初始化，先 `GET` 查询现状。
- **私有仓库 404/不可用**：免费版 Pages 仅支持 public 仓库；私有需付费订阅。
- **push 被拒**：确认 token 具备 `repo` scope；确认账号对该仓库有写权限。
- **更新不生效**：浏览器/CDN 缓存，强制刷新（Ctrl+F5）或稍等；确认改的是发布分支。
- **自定义域名**：见上文「自定义域名」小节——仓库根放 `CNAME` + DNS 解析 + Enforce HTTPS。

## 安全提醒

- 免费版 Pages 全网公开，禁止托管任何敏感数据、密钥、客户信息、私有报表。
- 不要把 PAT 写入提交或仓库文件；脚本只在内存和远程 URL 中使用 token。
