## Description: <br>
Agent Expression helps chat agents search, ingest, and emit local meme or sticker image paths using a local pack, SQLite search, and optional vision or embedding APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yyh-001](https://clawhub.ai/user/yyh-001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to let chat agents find appropriate local stickers by mood or keyword, add user-provided images to a local meme pack, and return real absolute image paths for host-specific delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can link or copy the skill into multiple agent environments and may update an existing checkout. <br>
Mitigation: Inspect the installer before running it, avoid piping remote scripts directly into a shell, and choose explicit install paths that do not contain important unrelated files. <br>
Risk: Optional ingest and captioning flows can send local images or captions to external AI APIs using configured credentials. <br>
Mitigation: Keep private images out of API-backed ingest flows and only configure API keys and base URLs for providers you trust. <br>
Risk: The server security verdict is suspicious because the skill modifies agent installations and can use ambient credentials for image analysis and embeddings. <br>
Mitigation: Review the installed files and security guidance before deployment, and limit credentials to the minimum needed for the selected workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yyh-001/skills/agent-expression) <br>
- [Host integration guide](references/hosts.md) <br>
- [Meme database schema](references/meme-db-schema.md) <br>
- [Meme embeddings schema](references/meme-embeddings-schema.md) <br>
- [Bundled pack credits](packs/official-001/CREDITS.md) <br>
- [Upstream bundled meme pack](https://github.com/anka-afk/astrbot-meme-pack-official-01) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and file path output conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search commands are expected to return real absolute local image paths; some hosts may require MEDIA: lines or file preview calls.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
