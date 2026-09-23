## Description:

Conduct open-ended research on a topic, building a living markdown document. Supports interactive and deep research modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brennerspear](https://clawhub.ai/user/brennerspear)

### License/Terms of Use:


## Use Case:

Developers, analysts, and external users use this skill to research topics, compare options, synthesize sources, and maintain living markdown research documents. It can also run deeper asynchronous research through Parallel AI and save results for later review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research prompts and findings may be saved under ~/.openclaw/workspace/research and deep-research prompts may be sent to Parallel AI.

Mitigation: Avoid sensitive or confidential prompts unless the user has approved the data handling path and reviewed the external service terms.

Risk: The setup guidance stores a Parallel AI API key through a persistent shell-profile export.

Mitigation: Prefer a scoped secret manager or per-command environment variable, and keep credential files permission-restricted.

Risk: The setup guidance includes a curl-to-shell installer path and optional system-wide symlinks.

Mitigation: Use a verified package-manager install path where possible, inspect installer sources before execution, and avoid system-wide installation unless required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/brennerspear/skills/research-agent)
- [OpenClaw](https://openclaw.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown research notes with source links, inline shell commands, and optional PDF exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores prompts and research findings under ~/.openclaw/workspace/research when used as documented.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
