## Description:

Generates clean, portable Markdown from Markdown, HTML, or plain-text inputs, with support for normalization, lint reports, table-of-contents generation, and platform-specific formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, documentation authors, and agent users can use this skill to normalize Markdown, convert HTML to Markdown, generate tables of contents, and adapt documents for GitHub, GitLab, Obsidian, Notion, or CommonMark workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file-writing and command-execution capabilities for ordinary Markdown cleanup.

Mitigation: Constrain use to known Markdown files and approved formatting or linting commands; avoid granting unrestricted shell access.

Risk: The skill includes API-key and network-oriented guidance that is not necessary for routine Markdown processing.

Mitigation: Do not provide API keys or network access unless a reviewed workflow specifically requires them.

Risk: Generated Markdown or lint guidance may be incorrect or misleading for a target platform.

Mitigation: Preview output in the target renderer and review lint findings before publishing or overwriting source documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/markdown-toolkit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured results containing converted Markdown, lint findings, table-of-contents entries, and metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file edits or command execution when the host agent grants read, write, or exec tools.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
