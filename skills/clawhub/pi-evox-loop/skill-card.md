## Description:

Helps coding agents recall reviewed fixes at task start, record useful fixes after failures, and optionally measure their impact in controlled experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to reuse reviewed fixes across coding tasks, capture new repairs, and optionally assess whether those fixes improve subsequent runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prior session or tool content can become persistent guidance for future agents.

Mitigation: Keep manual review enabled in shared or sensitive environments and audit stored fixes regularly.

Risk: Automatic approval can persist untrusted session content without review.

Mitigation: Avoid --auto-approve-lowrisk and --auto-approve on untrusted histories.

Risk: Optional LLM refinement can transmit transcript content to an external endpoint.

Mitigation: Use --llm-refine only after checking the endpoint and authorizing data sharing.

Risk: A fresh run can destructively reset stored experience despite backups.

Mitigation: Treat --fresh as destructive and confirm backups before using it.

## Reference(s):

- [ClawHub release listing](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage (publisher-listed)](https://github.com/stwhwing/pi-evox-lab)
- [Other agent integrations](docs/other-agents.md)
- [Experiment report](docs/experiment-report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create local fix records and optional experiment reports.]

## Skill Version(s):

0.14.6 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
