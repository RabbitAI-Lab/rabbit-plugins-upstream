## Description:

Generates eight categories of prompt-injection attack drills and expected-behavior checks for pre-launch red-team testing of a system prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, prompt engineers, and governance reviewers use this skill to generate repeatable prompt-injection drills and expected outcomes before deploying an agent or assistant prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes one-command global install guidance through a mutable installer.

Mitigation: Review the installer first, or install only reviewed prompt-injection-drill files from a pinned commit or verified archive.

Risk: The drill reads system prompts that may contain sensitive policy or internal instructions.

Mitigation: Run it only on prompt files intended for testing and keep generated outputs in approved locations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-injection-drill)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown drill checklist, with optional JSON output and optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local output from a zero-dependency Python script.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and release changelog mention 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
