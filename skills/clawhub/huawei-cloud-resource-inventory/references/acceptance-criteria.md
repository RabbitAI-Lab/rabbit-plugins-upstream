# 验收标准

## 功能验收

- [ ] 每类资源一张表，列出租户名下全部该类型实例
- [ ] 表内包含与其他资源的关联字段（所属 VPC/子网、挂载 EVS、所在集群等）
- [ ] 支持跨所有 region 聚合汇总
- [ ] 以代码块/纯文本表格形式输出
- [ ] 仅只读操作，不产生任何资源变更
- [ ] AK/SK 从环境变量读取，无硬编码敏感信息

## 命令验收

- [ ] `python3 scripts/resource_inventory.py --help` 显示帮助信息，退出码 0
- [ ] `python3 scripts/resource_inventory.py --capability-list` 列出支持的资源类型，退出码 0
- [ ] `python3 scripts/resource_inventory.py --region cn-north-4` 查询单 region 资源，退出码 0
- [ ] `python3 scripts/resource_inventory.py --resource-type ecs,vpc` 查询指定资源类型，退出码 0
- [ ] `python3 scripts/resource_inventory.py --format json` 输出 JSON 格式，退出码 0
- [ ] AK/SK 缺失时退出码 3，并给出明确提示

## 关联关系验收

- [ ] ECS 表包含 vpc_id、subnet_ids、volume_ids、public_ips 关联字段
- [ ] EIP 表包含 associated_server 字段，指向关联的 ECS 实例
- [ ] EVS 表包含 attached_to 字段，指向挂载的 ECS 实例
- [ ] Subnet 表包含 vpc_id 和 vpc_name 关联字段
- [ ] ELB 表包含 vpc_id 和 vpc_name 关联字段
- [ ] NAT 表包含 vpc_id 和 vpc_name 关联字段
- [ ] CCE 表包含 vpc_id、subnet_id、node_count 关联字段

## 安全验收

- [ ] 无硬编码 AK/SK/Token
- [ ] 数据来源为真实 API 返回，不使用虚构数据
- [ ] 错误处理完整（API 错误有提示，不静默崩溃）
- [ ] 所有 API 调用有 30s 超时
- [ ] 输入验证完整（参数校验防注入）
