# Manifest 说明（分发元数据）

`manifest/manifest.json` 是青田·心理学自学室的分发元数据**单源文件**，描述技能标识、能力清单、资源位置与数据约定，供 SkillHub / 多平台商店 / 版本校验工具读取。

## 用法

- **版本对齐**：`skill.version` 必须与 `SKILL.md` frontmatter 的 `version` 保持一致；发布新版本时同步更新。
- **能力清单**：`capabilities[]` 是给平台做能力发现用的稳定标识，不要随文案频繁变动。
- **数据约定**：`data.progress_file` 说明进度文件位置与 schema 路径，第三方集成方据此读写。
- **引用本文件**：README 已知边界中已声明 manifest 为分发元数据；后续若接入多平台（Claude/Copilot/Cursor 等）分发，可参考 clinical-toolkit 的做法由单一 manifest 生成各平台格式，但需在 CI 中校验生成物与单源一致（当前版本仅提供单源，未生成平台 manifests，避免未验证格式误导）。

## 校验

```bash
python -c "import json; json.load(open('manifest/manifest.json', encoding='utf-8')); print('manifest OK')"
```
