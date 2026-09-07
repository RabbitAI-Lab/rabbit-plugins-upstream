# 会话实录（给 AI 对齐"怎么用 + 怎么向用户汇报"）

> 以下为用户可见摘要的语气/粒度示范。真实输出以脚本 JSON 为准；汇报做到"先结论、再要点、询问是否需要细节"。

## 示例一：AIP 自然语言查数（首次使用场景，含安装引导）

**用户**：我想查一下各区域销售额排名，另外我还没装 ZY Action 平台。

**AI**：
- 尚未安装 → 进入安装引导（参照 SKILL.md 第三节）：打开 https://zyinfo.pro/action/ 下载 ZY-Action-Platform.rar；解压后复制 `config.yaml.example` 为 `config.yaml`，把 DeepSeek Key 填到 `llm.api_keys.deepseek`；若本机无 PostgreSQL 把 `database.type` 改成 `SQLite`；双击「运行AI商业行动系统-ZY Action.exe」启动；浏览器打开 http://127.0.0.1/ ，用 `admin/admin1` 登录（建议尽快改密）。
- 待用户确认装好并启动后，依次执行并汇报：

```bash
python3 scripts/zy_platform.py health --product aip
python3 scripts/zy_platform.py login --product aip --username <用户账号> --password <口令>
python3 scripts/zy_platform.py chat --product aip --query "各区域销售额 Top5"
```

**AI 汇报**：已按各区域销售额从高到低排好：① 华东 X 万元 ② 华南 Y 万元 …。SQL 为 `SELECT ...`，置信度 0.97（按需展示）。需要我把它做成图表/继续追问某区域明细吗？

## 示例二：AIP 自动化工作流——列出→运行→查结果

**用户**：帮我跑一下"库存补货建议"那个自动化。

**AI**：
```bash
python3 scripts/zy_platform.py workflow-list --product aip
python3 scripts/zy_platform.py workflow-run --product aip --workflow-id <id> --params '{"region":"华东"}'
python3 scripts/zy_platform.py workflow-status --product aip --execution-id <eid>
```
**AI 汇报**：工作流 `<名称>` 已执行完成（execution_id `xxxx`），状态 `completed`，共 4 个节点全部成功。关键结论：华东区有 3 个 SKU 低于补货点，建议补货量合计约 …。要看每个节点的详细输出吗？

## 示例三：跨产品 + 按安装目录自读文档

**用户**：我平台装在 D:\zyaction。想看看 Foundry 上有没有"订单"本体，再去 Gotham 搜下"玄武集团"相关情报。

**AI**（先读安装目录文档，再调用）：
```bash
# 1) 用 Read 看 D:\zyaction\README.md 确认端口/账号；必要时读 docs\manuals 与 api-demo 示例
# 2) 直连验证与登录
python3 scripts/zy_platform.py health --product foundry
python3 scripts/zy_platform.py login --product foundry --username <账号> --password <口令>
# 3) 找本体对象类型，找"订单"
python3 scripts/zy_platform.py ontology-objects --product foundry
python3 scripts/zy_platform.py ontology-search --product foundry --query "订单"
# 4) Gotham 情报搜索（Gotham 与 Foundry token 可共用，但各产品独立登录更稳）
python3 scripts/zy_platform.py search --product gotham --query "玄武集团" --limit 5
```
**AI 汇报**：Foundry 本体含 `order(销售订单)` 等类型，相关指标 2 个；Gotham 搜到 5 条：融合实体 1 个、时间轴事件 2 条（含"玄武集团高管会晤"）、地图点位 2 个。需要我展开某一域/生成简报吗？

## 常见失败与话术

- 退出码 2（连不上）→ "平台似乎没在运行，请双击启动器 .exe 后告诉我再试；或确认 --product 端口/--base-url 正确。"
- 退出码 4（401）→ "登录已过期，请重新提供平台账号口令，我再 login 一次。"
- 业务 code≠0 且提示 LLM 相关 → "请检查安装目录 config.yaml 里 `llm.api_keys.deepseek` 是否已填真实 Key 并重启平台。"
- 404 → "该版本可能没有此接口/路由名不同。可以用 `request` 对照随包 `API 接入及测试方法参考.txt` 试真实路径。"
