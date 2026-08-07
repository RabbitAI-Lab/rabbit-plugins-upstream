---
name: 员工XXX的相关案件查询
description: 查询员工作为被处理人｜被举报人的案件详情，注意该SOP不适用于 查询员工作为负责人的案件查询
---

# 员工XXX的相关案件查询

## 适用场景
查询员工作为被处理人｜被举报人的案件详情，注意该SOP不适用于 查询员工作为负责人的案件查询

## 输入参数
- 人员姓名

## 执行流程
> Claude 请严格按以下步骤依次查询数据表并分析，注意每一步的依赖关系、输入与输出字段。

```
step_1_1:xx作为被处理人
从表【jd_rcp_case_dispose_insider_new】输入人员姓名【namebdp】获取对应的案件编号,处理结果
step_1_2：xx出现在案件标题、描述、内容、摘要
从表【jd_rcp_case_info】输入人员姓名，筛选 title_search LIKE '%{name}%' 		OR summary_search LIKE '%{name}%' 		OR description_search LIKE '%{name}%' 		OR content_search LIKE '%{name}%' 来获取案件编号
step_2:查询案件的详情
从表【jd_rcp_case_info】中输入案件编号，获取案件详情，返回案件编号、案件名称、案件描述、案件状态、负责人、跟进部门、举报方式、调查结论、处理结果
依赖 step_1.casenum
```

---
_来源思维链ID: 2029845474681409818 ｜ owner: 张兴世（zhangxingshi.2） ｜ 创建时间: 2026-06-12 15:41:25 ｜ 最近更新: zhangxingshi.2 2026-07-20 14:00:17_
