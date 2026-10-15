## Description:

Helps coding agents recall reviewed fixes, record fixes to non-obvious failures for later reuse, and optionally measure their impact in controlled experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to recall relevant, reviewed repair guidance during coding tasks and retain useful fixes for future tasks. They can optionally run controlled experiments to assess whether reusing fixes helps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unreviewed or incorrect stored fixes can influence later agent work, especially when automatic approval or agent hooks are enabled.

Mitigation: Review generated fixes before approving them, and enable automatic approval or hook installation only deliberately.

Risk: Optional session distillation can read local session history, and optional refinement can send transcript text to a configured endpoint.

Mitigation: Check session contents and the destination before using these optional features; leave refinement disabled if transcripts must remain local.

Risk: A fresh run can reset the local experience store after creating a backup.

Mitigation: Confirm the backup and intended reset before using --fresh.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [Advanced usage and integrations](docs/advanced.md)
- [Security and license details](docs/security-and-license.md)
- [Controlled experiments](docs/research.md)

## Skill Output:

**Output Type(s):** [Repair guidance, Shell commands, Configuration instructions]

**Output Format:** [Text and Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relevant reviewed fixes are recalled from local experience records; new fixes require review before reuse unless automatic approval is enabled.]

## Skill Version(s):

0.20.3 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
