# Style Validator - 风格验证器

## Style Score（7 维度评分）

生成 Prompt 前先自检。对编译后的 Prompt 评分：

| 维度 | 评分项 |
|------|--------|
| Budget Authenticity | 低成本真实性 - 是否像真的没钱做的 |
| Character Roughness | 角色粗糙度 - 建模是否足够粗糙 |
| Texture Simplicity | 贴图简洁度 - 贴图是否足够简单 |
| Environment Roughness | 场景粗糙度 - 场景是否和角色一样粗糙 |
| Lighting Simplicity | 灯光简洁度 - 灯光是否足够简单 |
| Rendering Imperfection | 渲染不完美度 - 渲染质量是否足够低 |
| Uncanny Awkwardness | 笨拙感 - 比例/表情/动作是否足够笨拙 |

每项 0-100，总分 0-100。

### 评分示例

```
Budget Authenticity     91
Character Roughness     88
Texture Simplicity      93
Environment Roughness   86
Lighting Simplicity     82
Rendering Imperfection  89
Uncanny Awkwardness     84

TOTAL                   88
```

### 判定规则

- 总分 >= 75：PASS，输出最终 Prompt
- 总分 < 75：FAIL，回退至 Step 6 重新编译

## 风格漂移检测

检测 Prompt 是否出现以下高级词：

```
Pixar
Disney
cinematic
beautiful
premium
hyperrealistic
photorealistic
detailed
luxury
high-end
AAA
ray tracing
realistic fur
PBR
```

一旦出现，自动处理：

| 漂移词 | 替换为 |
|--------|--------|
| cinematic lighting | simple direct lighting |
| realistic fur | simple painted texture |
| premium 3D | rough low-budget CGI |
| beautiful composition | simple centered composition |
| high-end CGI | outdated CGI rendering |
| photorealistic | low-resolution CGI |

残留高级词 = FAIL，需重新编译。

## 风格判断标准

生成结果必须同时满足：

```
粗糙模型       ✓
比例失衡       ✓
动作僵硬       ✓
眼神木讷       ✓
嘴巴突出       ✓
简单贴图       ✓
真实毛发      ✗
高级材质      ✗
电影灯光      ✗
Pixar感       ✗
高级CG        ✗
场景精致      ✗
```

最核心的判断问题：

> "如果把这张图放到一部2005年前后的国产儿童3D动画里，会不会毫无违和感？"

如果答案是"不会"，说明风格跑偏。
