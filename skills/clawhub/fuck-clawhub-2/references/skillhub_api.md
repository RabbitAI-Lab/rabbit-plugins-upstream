# SkillHub 公开 API 参考（skillhub.cn）

SkillHub 提供免鉴权的公开列表接口，本 skill 全部基于它实现搜索与链接转换。

## 列表接口（搜索）

```
GET https://api.skillhub.cn/api/skills
```

### 请求参数（query string）

| 参数      | 必填 | 说明                                                         |
| --------- | ---- | ------------------------------------------------------------ |
| keyword   | 是   | 关键词，分词搜索（中英文均可）。不要用 `/api/v1/search`。    |
| sortBy    | 否   | 排序字段。`score`=相关度（默认推荐）、`downloads`=下载量等。 |
| category  | 否   | 一级分类过滤，如 `office-efficiency`、`knowledge-management`。 |
| pageSize  | 否   | 每页数量，默认 10。                                          |
| page      | 否   | 页码，从 1 开始。                                            |

示例：
```
https://api.skillhub.cn/api/skills?keyword=pdf&sortBy=score&pageSize=10
https://api.skillhub.cn/api/skills?keyword=ocr&category=office-efficiency&pageSize=5
```

### 响应结构

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "total": 2165,
    "skills": [
      {
        "name": "PDF和图片文字提取",
        "slug": "pdf-image-text-extractor",
        "version": "1.0.9",
        "ownerName": "user_5f9c21aa",
        "updated_at": 1785058166251,
        "created_at": 1775788233472,
        "category": "office-efficiency",
        "description": "...",
        "description_zh": "...",          // 优先使用此字段作“简介”
        "score": 81435.59,                // 相关度，sortBy=score 时降序
        "downloads": 42756,
        "installs": 378,
        "stars": 87,
        "verified": false,
        "source": "community",
        "homepage": "https://api.skillhub.cn/user_5f9c21aa/pdf-image-text-extractor",
        "namespace": {
          "canonicalName": "@user_5f9c21aa/pdf-image-text-extractor",
          "displayName": "user_5f9c21aa",
          "publicSlug": "pdf-image-text-extractor"
        }
      }
    ]
  }
}
```

### 输出所需的 5 个字段映射

| 用户要求   | API 字段          | 处理                                          |
| ---------- | ----------------- | --------------------------------------------- |
| 名称       | `name`            | 直接使用                                      |
| 版本号     | `version`         | 直接使用                                      |
| 作者       | `ownerName`       | 直接使用（或 `namespace.displayName`）        |
| 更新日期   | `updated_at`      | 毫秒时间戳 → `YYYY-MM-DD`                     |
| 简介       | `description_zh`  | 缺省回退 `description`，去换行、截断到 ~120 字 |

## 链接格式

- SkillHub 技能页：`https://skillhub.cn/skills/<slug>`
- ClawHub 技能链接：`https://clawhub.ai/<namespace>/<slug>`
- 转换思路：解析 ClawHub 链接得到 `<slug>`，在 SkillHub 按该词搜索，匹配同名/同 slug 即给出 SkillHub 链接。

## 安装命令（SkillHub CLI）

```bash
# 先装 CLI（如尚未安装）
curl -fsSL https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash -s -- --cli-only

# 安装某个 skill，必须 --dir 指向当前 Agent 的 skills 目录
skillhub install <slug> --dir <skills 目录>
```

- WorkBuddy 用户级：`~/.workbuddy/skills`
- WorkBuddy 项目级：`<workspace>/.workbuddy/skills`

> 注意：SkillHub 社区 skill 未必都经过与 ClawHub 同等严格的审查；SkillHub 自带“双实验室安全审计”可作为参考。安装前建议先核对作者、更新时间与简介，必要时审阅源码。
