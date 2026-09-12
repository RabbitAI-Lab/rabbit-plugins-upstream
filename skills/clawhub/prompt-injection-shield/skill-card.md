## Description:

Prompt Injection Shield scans untrusted web, email, tool, retrieval, or uploaded text before it enters an AI context, using bilingual prompt-injection patterns and heuristics to return a risk score, matched rules, and a drop, quarantine, or pass action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to screen external content before passing it to an LLM or agent workflow, especially for RAG, email processing, web scraping, uploads, and tool outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published install commands may fetch mutable or unpinned content.

Mitigation: Install from a pinned release or commit and verify the provided file hashes before use.

Risk: The scanner processes local text or files supplied by the user.

Mitigation: Review the local script, install it only into the intended agent profile, and pass only content that should be scanned.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-injection-shield)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with optional CLI text or JSON scan output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk score from 0 to 100, matched rule details, recommended action, and process exit code]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest.json; SKILL.md frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
