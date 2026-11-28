# skillhub-publish-skill

## 开发 / clone 后

新 clone 跑一次 `python scripts/install_hooks.py`，会配好 Git hooks：`pre-commit` 守住脚本必须入库，`post-commit` 在提交后自动推送当前分支；验收用 `python scripts/install_hooks.py --check`。`core.hooksPath` 是本地配置、不随 push 走，每个 clone 都要跑一次。临时只提交不推用 `AI_SKIP_AUTOPUSH=1 git commit ...`。
