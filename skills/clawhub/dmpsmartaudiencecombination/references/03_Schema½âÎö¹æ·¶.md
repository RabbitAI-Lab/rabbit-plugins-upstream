# 03 Schema解析规范（10维）

> 对齐：你提供的 `semantic-schema_2.md`。

## 1. 解析目标
将用户自然语言需求解析为 10 维 Schema（解析框架，不是问卷）。

## 2. Schema骨架（示意）
```json
{
  "market": "",
  "objective": "",
  "audience": {
    "demographics": {},
    "location": {},
    "behavior": {},
    "scene": {},
    "interest": {},
    "lifestyle": {},
    "kol_koc": {},
    "activity": {}
  },
  "industry_ext": {},
  "constraints": {}
}
```

## 3. 解析规则
1) 用户没说的不填；禁止按常识补全。
2) 模糊词能转译则转译；转译失败触发最小追问。
3) 用户明确排除 → 写入 constraints（EXCLUDE）。
4) objective 缺失 → 可默认，但要标记 defaulted=true。

## 4. 输出要求
- 数值字段用结构化值（如年龄段 25-34）。
- 每个字段附 priority（MUST/PREFERRED/OPTIONAL/EXCLUDE），后续用于选择与组合。

## 5. 示例（简）
输入："精致女孩，护肤美妆兴趣，一二线城市，最近活跃"
- demographics.gender=female（倾向）
- interest=护肤/美妆
- location.city_level=一线/新一线
- activity=近30天/近60天
