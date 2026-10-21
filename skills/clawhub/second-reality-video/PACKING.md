# Packaging rules

SkillHub **rejects dotfiles** in an upload (`400 不允许的文件类型: .gitignore` /
`.skillhubignore`), so this package keeps its exclusion list here instead of in an ignore file.

When packaging or publishing, make sure the archive contains **only** these entries:

```text
SKILL.md
README.md
PACKING.md
LICENSE
package.json
scripts/second-reality-video-client.mjs
scripts/mock-service.mjs
references/api.md
references/shot-files.md
references/determinism.md
```

Never include:

```text
.state/        # session state: bill + original request (contains order data)
node_modules/  # installed dependencies
.env / .env.*  # environment files
out/           # downloaded artifacts
*.log          # runtime logs
__pycache__/   # bytecode
*.pyc
```

Check before publishing:

```bash
skillhub publish . --version 1.0.0 --dry-run
```

`--dry-run` validates the frontmatter and the manifest client-side, but it does **not** catch
server-side file-type rejections — publish once and read the server response.
