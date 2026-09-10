## Description:

Generates high-contrast, resonant, story-driven spoken scripts for short videos, character stories, and personal IP viewpoint scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to turn a persona, pain point, or topic into a colloquial short-video spoken script with a seven-step story structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is advertised for spoken-script writing but includes guidance to install and use a third-party dLazy CLI.

Mitigation: Review the skill before installation and only install or invoke the CLI when a dLazy integration is intentionally required.

Risk: Prompts and selected media may be sent to dLazy services during CLI-backed workflows.

Mitigation: Avoid sensitive or confidential inputs unless external processing by dLazy services is approved for the use case.

Risk: The dLazy API key can be stored locally for CLI authentication.

Mitigation: Protect the local credential, prefer scoped or disposable keys where available, and rotate or revoke keys from the dLazy dashboard when access changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text or Markdown spoken-script drafts with optional shell command snippets for dLazy CLI use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts are structured around a seven-step short-video narrative pattern and may be tailored from user-provided persona, pain point, or topic details.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
