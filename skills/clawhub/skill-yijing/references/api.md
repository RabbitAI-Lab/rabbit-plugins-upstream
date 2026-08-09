# 天玑八卦盘 — API 参考

Base URL: `https://skill.aiepco.com`

## 认证

所有 API 使用 Bearer Token 认证：

```
Authorization: Bearer sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## 端点

### 1. 起卦 — `POST /api/yijing/cast`

消耗：10 Token

```json
// 铜钱起卦
{ "method": "coins" }

// 时间起卦
{ "method": "time" }

// 数字起卦
{ "method": "number", "params": { "n1": 23, "n2": 47, "n3": 89 } }

// 随机起卦
{ "method": "random" }
```

返回：

```json
{
  "success": true,
  "data": {
    "method": "coins",
    "original_hexagram": {
      "number": 1,
      "name": "乾为天",
      "upper": "☰",
      "lower": "☰",
      "judgment": "元亨利贞",
      "image": "天行健，君子以自强不息",
      "brief": "创始通达，利于坚守正道..."
    },
    "changed_hexagram": { /* 同上结构，无动爻时为 null */ },
    "changing_lines": [3, 5],
    "lines": [7, 7, 9, 7, 9, 7]
  },
  "usage": { "charged": 10, "remaining": 90 }
}
```

六爻数值：
- 6 = 老阴（变阳爻）
- 7 = 少阳
- 8 = 少阴
- 9 = 老阳（变阴爻）

### 2. AI 解卦 — `POST /api/yijing/read`

消耗：20 Token

```json
{
  "hexagram": { /* 本卦信息 */ },
  "changed_hexagram": { /* 变卦信息，可为 null */ },
  "changing_lines": [3, 5],
  "lines": [7, 7, 9, 7, 9, 7],
  "method": "coins",
  "question": "我这个月适合换工作吗？"
}
```

返回：

```json
{
  "success": true,
  "data": {
    "interpretation": "## 卦象总览\n\n乾为天卦象显示..."
  },
  "usage": { "charged": 20, "remaining": 70 }
}
```

### 3. 自动注册 — `POST /api/tools/auto-register`

免费，无需认证。

```json
// 无需请求体
```

返回：

```json
{
  "success": true,
  "user_id": "uuid",
  "username": "灵机_a3bxk7",
  "password": "xK9m!pQw2$",
  "api_key": "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "tokens": 20,
  "message": "账号已自动创建！20 Token 已到账。"
}
```

### 4. 用户资料 — `GET/PUT /api/tools/profile`

需要认证。

**GET** — 获取资料：

```json
{
  "username": "灵机_a3bxk7",
  "email": "uuid@skill.aiepco.auto",
  "email_changed": false,
  "can_change_email": true,
  "tokens": 20,
  "key_tokens_remaining": 20
}
```

**PUT** — 修改资料：

```json
{
  "username": "新用户名",
  "email": "real@email.com",
  "new_password": "newPass123",
  "current_password": "oldPass456"
}
```

⚠️ `email` 仅可修改一次，`email_changed=true` 后不可再次修改。

## 错误码

| 状态码 | 说明 |
|:---|:---|
| 400 | 参数错误 |
| 401 | API Key 无效或未提供 |
| 402 | Token 余额不足 |
| 403 | 操作被拒绝（如邮箱已修改过） |
| 409 | 邮箱已被占用 |
| 503 | AI 服务不可用 |
