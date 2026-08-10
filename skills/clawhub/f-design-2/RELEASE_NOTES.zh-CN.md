# design-guide v0.1.1

`v0.1.1` 是一次修复发布，保留 `v0.1.0` 的完整设计到实现工作流，并加强发布完整性、密钥扫描、版本一致性和跨 AIDE 同步安全。

升级命令：

```bash
git pull --ff-only
bash scripts/sync-aide.sh
python3 scripts/design-guide-doctor.py --strict
```
