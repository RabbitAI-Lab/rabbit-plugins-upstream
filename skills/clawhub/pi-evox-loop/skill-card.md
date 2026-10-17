## Description:

Helps coding agents recall reviewed fixes, record newly learned fixes, and optionally measure their value in controlled experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to recall and review fixes at the start of coding tasks, record useful repairs for later reuse, and optionally test whether recalled fixes improve subsequent runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored or imported fixes may influence future agent prompts.

Mitigation: Review generated and imported fixes before approval and keep the default human review gate enabled.

Risk: Optional refinement or gene sharing may send sensitive session information outside the machine.

Mitigation: Leave these features off unless you have checked what will be shared and approved the destination.

Risk: Enabling hooks or adding snippets to project instructions may change future agent behavior.

Mitigation: Inspect dry-run output before enabling hooks or changing project instructions.

## Reference(s):

- [Pi EvoX Loop on ClawHub](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [Advanced usage](docs/advanced.md)
- [Frequently asked questions](docs/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown with numbered fixes and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can store reviewed fixes locally for later recall and produce optional experiment reports.]

## Skill Version(s):

0.21.0 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
