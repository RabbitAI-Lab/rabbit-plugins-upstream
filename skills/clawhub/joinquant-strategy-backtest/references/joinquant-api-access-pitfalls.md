# JoinQuant API 文档获取陷阱记录

> 2026-08-10 实测记录，供未来session参考，避免重复踩坑。

## 背景

需要获取聚宽API文档内容（https://www.joinquant.com/help/api/help#name:api）以构建策略开发技能。

## 尝试记录

### 1. curl 直接访问 JoinQuant 帮助页面

```
curl -sL "https://www.joinquant.com/help/api/help" \
  -H "User-Agent: Mozilla/5.0 ..."
```

**结果：** 返回7KB HTML框架，全是CSS/JS引用，无API正文内容。
**原因：** 聚宽文档是JavaScript SPA，内容由前端JS动态渲染，curl只能拿到空壳。

### 2. 搜狗网页搜索

```
curl -sL "https://www.sogou.com/web?query=聚宽+joinquant+API+文档"
```

**结果：** 5.4KB响应，全是JS反爬代码（SNUID cookie验证、验证码逻辑），0条搜索结果。
**原因：** 搜狗对程序化请求触发反爬，返回JS验证页面而非搜索结果。与 cn-web-search skill 文档一致："搜狗网页对连续批量请求触发反爬"。

### 3. 百度搜索

```
curl -sL "https://www.baidu.com/s?wd=聚宽+joinquant+API+文档"
```

**结果：** 1.4KB响应，0行有效文本。百度反爬返回空壳。
**原因：** 百度对无cookie的curl请求返回空内容。与 cn-web-search skill 文档一致。

### 4. GitHub jqdatasdk 仓库

```
curl -sL "https://raw.githubusercontent.com/JoinQuant/jqdatasdk/master/README.md"
```

**结果：** 获取到README，但内容是产品营销介绍（公司背景、产品定位、数据分类），不含策略API参考文档。
**发现：** README中提到JQData数据API文档在另一个URL：`https://www.joinquant.com/help/api/doc?name=JQDatadoc`（不同于策略API的help页面）。
**GitHub搜索：** 搜索 `joinquant strategy` 找到24个仓库，Top1是 `JizhiXiang/Quant-Strategy`（含ML决策树示例，非API文档）。

### 5. Wayback Machine

```
curl -sL "https://web.archive.org/cdx/search/cdx?url=www.joinquant.com/help/api/help&output=json"
curl -sL "https://web.archive.org/web/2024/https://www.joinquant.com/help/api/help#name:api"
```

**结果：** CDX API超时（15秒），直接访问也超时（20秒）。
**原因：** web.archive.org 在当前环境不可达或响应极慢。

### 6. browser_navigate 工具

```
browser_navigate(url="https://www.joinquant.com/help/api/help#name:api")
```

**结果：** Chrome启动失败。
**错误：** `FATAL:content/browser/zygote_host/zygote_host_impl_linux.cc:128 No usable sandbox!`
**原因：** 当前Linux环境（Ubuntu 23.10+或类似）禁用了unprivileged user namespaces，Chrome sandbox无法工作。
**可能的修复：** 提示建议使用 `--no-sandbox` 参数，但未在当前session验证是否可行。

## 结论与可行方案

| 方案 | 可行性 | 说明 |
|------|:------:|------|
| 依赖模型训练知识 | ✅ 已验证 | 模型对聚宽API有较好的训练知识，骨架准确（initialize/handle_data/order等核心函数） |
| 用户贴文档内容 | ✅ 最可靠 | 让用户直接将API文档内容复制到对话中 |
| --no-sandbox浏览器 | ⚠️ 未验证 | 可尝试在browser_navigate中传参，但不确定工具是否支持 |
| jqdatasdk源码 | ⚠️ 有限 | 可从 `JoinQuant/jqdatasdk/jqdatasdk/` 目录的Python源码中反推数据API签名 |
| CSDN/知乎博客 | ⚠️ 未尝试 | 可能有第三方博客转载了API文档，但搜索引擎不可用时无法发现 |

## 环境信息

- 测试环境：阿里云ECS (<YOUR_SERVER_IP>)
- curl可用，但出站网络对部分站点有限制
- Chrome浏览器无法启动（sandbox限制）
- 搜狗/百度搜索均触发反爬
- web.archive.org不可达
