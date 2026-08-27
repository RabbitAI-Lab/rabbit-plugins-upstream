# 验收标准

## 功能验收

| 编号 | 验收项 | 验证方法 | 通过标准 |
|------|--------|----------|----------|
| AC1 | AK/SK 环境变量配置，不硬编码 | 检查脚本无硬编码密钥；grep AK/SK 值无匹配 | 凭据从环境变量动态扫描读取 |
| AC2 | 列表查询返回 JSON 实例列表 | `python3 scripts/huawei-cloud-ecs-list.py list --region cn-north-4` | 输出 `{"count":N,"servers":[...]}` |
| AC3 | 详情查询返回 JSON 完整信息 | `python3 scripts/huawei-cloud-ecs-list.py show --server-id <ID>` | 输出 `{"server":{...}}` 含全部字段 |
| AC4 | 实例含全部字段 | 检查 list/show 输出字段 | 含 ID/名称/状态/公网IP/私网IP/规格/区域/创建时间/镜像/VPC/子网/安全组/磁盘等 |
| AC5 | 支持区域/状态/名称/规格过滤 | `list --region X --status Y --name Z --flavor W` | 返回过滤后结果 |
| AC6 | 无实例返回空列表 | 查询无实例的区域 | 返回 `{"count":0,"servers":[]}` 非报错 |
| AC7 | 实例 ID 无效明确错误 | `show --server-id invalid` | stderr 输出错误提示，退出码 2 |
| AC8 | AK/SK 缺失明确错误 | unset AK/SK 后执行 | stderr 输出错误提示，退出码 3 |
| AC9 | 独立设计 | 不依赖 scripts/greet.py | 无 import/引用现有实现 |
| AC10 | 使用说明 | `--help` / SKILL.md | 有完整使用说明 |

## 安全验收

- [ ] 无硬编码 AK/SK/Token
- [ ] 不使用 mock 模式/假数据（禁止 mock）
- [ ] 所有 API 调用有 30s 超时
- [ ] 错误处理完整（不静默崩溃）
- [ ] 参数校验防注入

## 结构验收

- [ ] SKILL.md ≤ 500 行，含必填段落
- [ ] frontmatter 含 name/description/version/triggers/tags
- [ ] name 与目录名一致
- [ ] references/iam-policies.md 存在
- [ ] templates/test-vars.json 存在
- [ ] 入口脚本可执行
- [ ] 总文件数 ≤ 30，总大小 ≤ 40MB
