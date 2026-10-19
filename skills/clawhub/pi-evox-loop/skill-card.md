## Description:

Helps coding agents recall reviewed fixes, record fixes they use, and save new lessons from difficult repairs, with optional controlled experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to help coding agents reuse reviewed solutions to recurring problems, save useful repairs for later tasks, and optionally compare performance in controlled experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored or imported fixes can influence future agent responses.

Mitigation: Review fixes and their source before approving or applying them; keep the experience store only if persistent agent memory is desired.

Risk: Trusted-pool settings and automatic approval can reduce review of shared fixes.

Mitigation: Inspect imported genes before trusting them, especially when using --tier official; retain manual approval where practical.

Risk: Optional refinement or session analysis may expose sensitive task or session content.

Mitigation: Only enable --llm-refine with an appropriate endpoint and avoid processing sensitive session logs unless local analysis is intended.

Risk: Fresh-start or confirmed installation commands can replace stored state or modify agent configuration.

Mitigation: Check backups and target paths before using --fresh or --yes install commands.

## Reference(s):

- [Pi EvoX Loop release](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage and documentation](https://github.com/stwhwing/pi-evox-lab)
- [Security and license guidance](docs/security-and-license.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown with numbered fixes and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relevant reviewed fixes are suggested at task start; no match may yield no suggested fix.]

## Skill Version(s):

0.24.0 (source: server release metadata, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
