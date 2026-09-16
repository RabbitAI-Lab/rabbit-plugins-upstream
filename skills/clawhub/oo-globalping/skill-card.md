## Description:

Provides Globalping actions through the OOMOL oo CLI for creating measurements, checking limits and credits, retrieving measurement results, and listing online probes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Globalping network measurements and inspect account limits, measurement status, results, and available probes through an OOMOL-connected Globalping account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute a remote oo CLI installer directly in a shell.

Mitigation: Prefer an official package-manager or verified release installation path, and use the remote installer only after reviewing and trusting the OOMOL installer source.

Risk: The create_measurement action changes Globalping state and may consume account quota or credits.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Globalping homepage](https://globalping.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-globalping)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
