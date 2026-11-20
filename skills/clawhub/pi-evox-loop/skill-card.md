## Description:

Helps coding agents recall validated fixes, record useful new fixes, and optionally run controlled experiments to measure reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use it to reuse validated fixes across coding tasks and capture lessons from non-obvious failures. Its optional experiment flow measures the effect of recalling those fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persisted fixes can become guidance in later agent prompts, and ClawScan flags concerns around automatic approval of reusable fixes.

Mitigation: Review new or shared fixes before approving them, and inspect recalled fixes before acting on them.

Risk: Optional model-backed flows can send task text, code, or transcripts to a configured external provider.

Mitigation: Keep these opt-in flows disabled unless needed; remove private content before sending and use a trusted endpoint.

Risk: ClawScan rates the release suspicious with high confidence, and scanner coverage is incomplete.

Mitigation: Review the package security and configuration guidance before installation, and enable optional features only after reviewing their data flow.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project overview](docs/overview.md)
- [Capability boundaries and triggers](docs/boundary-and-triggers.md)
- [Security and license details](docs/security-and-license.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Code, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands, code snippets, configuration examples, and JSON fix records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include retrieved fix summaries and review or provenance metadata.]

## Skill Version(s):

0.43.0 (source: skill frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
