## Description:

Diagnoses GitHub Actions to ClawHub publishing failures, including workflow references, owner and token setup, slug issues, pending-publication states, and skill directory discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose failed GitHub Actions publishing workflows for ClawHub skills and identify whether the issue is in workflow configuration, owner/token setup, slug validation, registry status, or skill directory discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow logs or configuration shared for diagnosis may expose sensitive operational details if pasted wholesale.

Mitigation: Share only the excerpts needed for diagnosis and redact token values, secret names, and private repository details before use.

Risk: Much of the bundled documentation is in Chinese, which may slow review or adoption for teams that need English-only operational guidance.

Mitigation: Have a bilingual reviewer confirm the troubleshooting guidance before relying on it in an English-only release workflow.

## Reference(s):

- [Failure Map](references/failure_map.md)
- [Project Homepage](https://github.com/bonniegeng-max/openclaw-publisher)
- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/github-actions-clawhub-doctor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with diagnostic findings, evidence references, and suggested commands or configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include minimal workflow or command snippets when relevant]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
