# 心灵补手 V3.5.0 — 常见问题 (FAQ)

> 针对 SkillHub 评测「反模式与FAQ 3.3」低分项的改进：补齐常见问题解答，遇到问题先查这里。

---

## 一、安装 / 环境

### Q1: 安装后运行 `xinling` 提示找不到命令？
**原因**：`xinling` 未加入 PATH。
**解决**：安装脚本会自动尝试链接到 `~/bin` 或 `~/.local/bin`。若仍不行，手动加：
```bash
export PATH="$HOME/.xinling-bushou-v2:$PATH"
# 或创建软链
ln -sf ~/.xinling-bushou-v2/xinling ~/bin/xinling
```

### Q2: 安装后 `xinling list` 只显示 5 个人格，刘伯温不见了？
**原因**：运行时目录 `~/.xinling-bushou-v2` 是旧版本残留，缺新人格。
**解决**：重新同步项目源码：
```bash
cd <项目目录>/xinling-bushou-v2
./scripts/install.sh
```
或手动覆盖 `~/.xinling-bushou-v2/personas/`。

### Q3: `xinling check` 显示某个「人格加载失败」？
**原因**：该人格 JSON 格式有误或缺字段。
**解决**：按 `check` 输出的 💡 提示修复对应文件；或删掉该文件后 `xinling add <id> <标准格式.json>` 重新导入。多数情况下重装可解决。

---

## 二、人格切换

### Q4: 为什么切换人格后「突然没声音了」/ 激活报错？
**V3.5.0 已修复根因**：旧版 5/6 个人格用非标准 JSON 结构，引擎读取时抛 KeyError 崩溃。
**当前状态**：V3.5.0 加入结构归一化器，任意格式都能稳定激活。若仍异常，先跑 `xinling check` 确认为 0 失败，再试 `xinling test <persona_id>`。

### Q5: 怎么知道当前激活了哪个人格？
```bash
xinling list          # 查看所有已注册人格
xinling show <id>     # 查看某个人的详情/触发词
```
会话级激活状态存在 `~/.xinling-bushou-v2/sessions/`。

### Q6: 能把 6 个人格同时叠加吗？
可以。`activate_persona` 的 `relationship=STACK` 支持叠加，会话栈可同时持有多个。但**不建议超过 2 个**，会互相抢占话术、导致风格混乱。

---

## 三、玄学测算（刘伯温）

### Q7: 刘伯温的测算怎么触发？
用户输入预测/测算/问事/迷茫类内容（如"算一卦""最近好迷茫""什么时候能成功"）时自动触发。也可手动 `bash scripts/heixiang.sh "你的问题"`。

### Q8: 测算依赖什么？失效了怎么办？
依赖 `core/heixiang_fusion.py`（六爻+奇门双法）。若外部模块缺失导致黑箱引擎不可用，**刘伯温会降级为纯口吻陪伴**，不再输出卦象判词，但对话仍正常。请务必安装依赖：
```bash
pip install -r requirements.txt   # 若项目提供
```

### Q9: 测算结果能当现实决策依据吗？
**不能。** 玄学测算仅作娱乐与心理陪伴用途。涉及医疗、投资、法律等重大决策，请理性评估，勿依赖测算结论。

---

## 四、行为 / 触发

### Q10: 触发词有情绪词，会不会误触发？
会。触发词含感叹词（啊/呀/哇/天哪）和情绪词（累/烦/崩溃），正常感叹或吐槽也可能触发谄媚。若不需要，可关掉：
```bash
xinling activate <persona_id> --level <N>   # 调低程度
# 或在人格 JSON 的 behavior.activation.always_on=false
```

### Q11: 话术重复度高怎么办？
V3.5.0 各人格语料（corpus/）含大量扩展种子。若仍觉重复，可编辑 `corpus/*.json` 增补，或调整 `behavior.frequency`（`min_rounds_between` / `max_per_session`）。

---

## 五、兼容 / 其他

### Q12: 支持哪些平台？
openclaw / claude_code / cursor / copilot / roo_code / aider / generic。见 `schemas/launch_config.py`。

### Q13: 为什么 SOUL.md 里看到「谄媚模块 v3.0 / v3.5.0」？
那是注入的人格片段，版本号取自你**注入时**的引擎版本。V3.5.0 注入会显示 `v3.5.0`。旧会话残留 `v3.0` 属正常，重跑 install.sh 重新注入即可更新。

### Q14: 出错了想彻底卸载？
```bash
rm -rf ~/.xinling-bushou-v2          # 删除运行时
# 并从 SOUL.md 移除注入的人格片段块
```
