# WorkBuddy 专家包约定

依据《WorkBuddy 专家开发规范》v2.4（2026-07-31）。本skill可独立复用，也随单Agent型专家包发布。

## 包布局

```text
aidso-geo-product-diagnostic/
  .codebuddy-plugin/plugin.json
  .mcp.json
  avatars/expert.png
  agents/aidso-geo-product-diagnostic.md
  skills/aidso-geo-product-diagnosis/
    SKILL.md
    references/
    scripts/
    assets/
    examples/
  README.md
```

Agent与skills在包根目录，不放进`.codebuddy-plugin`。点号路径为WorkBuddy约定的配置名称，不为文件添加文件系统hidden属性。

## 元信息与一致性

- `name`小写连字符、版本使用语义版本；英文description、author.name/email完整。
- `expertType=agent`；`agentName`等于Agent文件名和frontmatter.name；`plugin=name`。
- Agent frontmatter不得声明`tools`，权限由系统分配。
- 展示名称、职业、描述、默认提示及3个标签、3条快捷提示中英双语；默认提示等于首条快捷提示。中文展示描述40—50字。
- skills路径必须实际包含SKILL.md。
- 头像使用既有爱搜专家图，512×512 PNG，不超过500KB；不得使用外链头像。
- `dependencies.mcpServers`显式指向`./.mcp.json`。

## MCP设置

远程传输`type: http`，HTTPS服务。`headers.aidso-token`为`${AIDSO_TOKEN}`；`x-workbuddy.auth.type: token`，`tokenSchema.fields[].key`与占位符一一对应，输入类型password。名称、说明、图标、Token帮助入口完整。真实Token由WorkBuddy用户本地配置，包内只有表单契约。

## 交付边界

可验证本地目录结构、字段契约、离线算法、真实原始数据回放、HTML浏览器显示和ZIP解包运行。市场名称是否唯一、实际Token配置、线上调用与计费、WorkBuddy安装成功和市场审核必须单独以实际证据验证；未执行时如实标记待验证。

打包只包含专家运行所需文件，不包含客户原始数据、当前客户统计、工作机绝对路径、真实任务编号、账号凭据、缓存、历史包、.DS_Store、__MACOSX或开发记录。ZIP保留一个专家根目录。
