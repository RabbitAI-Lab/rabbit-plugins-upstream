# MCP Server 接入

cruise-product —— 由 CruiseSkillBridge 一键发布的MCP。

## 平台网关 Remote URL

```
https://cruise-mcp.olavacations.com/api/gw/mcp/63460e43-c726-44dc-8ae3-28841083d243
```

## server.json

```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json",
  "name": "io.github.309441738/cruise-product",
  "description": "cruise-product —— 由 CruiseSkillBridge 一键发布的MCP。",
  "version": "0.1.0",
  "remotes": [
    {
      "type": "streamable-http",
      "url": "https://cruise-mcp.olavacations.com/api/gw/mcp/63460e43-c726-44dc-8ae3-28841083d243"
    }
  ]
}
```

安装本 Skill 后，在 OpenClaw 配置中将 MCP remotes 指向上述 URL。
