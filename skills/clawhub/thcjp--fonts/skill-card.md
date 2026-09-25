## Description:

Provides web typography selection, font loading optimization, rendering diagnostics, and typography hierarchy guidance for Chinese, Western, and mixed-language websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to choose font pairings, build font-family fallback stacks, optimize web font loading, diagnose rendering issues, and generate CSS or typography system guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad write, command execution, API, and file-processing authority for typography-related work.

Mitigation: Install and use it only in workspaces where file modification and font-related command execution are acceptable, and require confirmation before commands or file writes.

Risk: API keys may be requested without a clearly scoped service or purpose.

Mitigation: Avoid providing API keys unless the exact service and purpose are clear, and pass any required secrets through environment variables rather than hardcoding them.

Risk: Font recommendations or generated CSS may affect page rendering, performance, licensing, or accessibility.

Mitigation: Review generated font stacks, @font-face declarations, license assumptions, and accessibility impact before deploying changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/fonts)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CSS, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include font recommendations, @font-face CSS, fallback stacks, typography scales, performance notes, and troubleshooting steps.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
