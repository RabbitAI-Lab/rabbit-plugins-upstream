## Description:

Mezmo (mezmo.com). Use this skill for ANY Mezmo request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Mezmo ingestion status and retrieve usage summaries grouped by app, host, or tag through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives the agent broad OOMOL CLI authority and includes unverified remote installer commands.

Mitigation: Review before installing, run the oo CLI installer only from a trusted source, prefer a verified package or checksum, and limit execution to documented Mezmo read actions where possible.

## Reference(s):

- [ClawHub Mezmo skill page](https://clawhub.ai/oomol/skills/oo-mezmo)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Mezmo homepage](https://www.mezmo.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include retrieved Mezmo status or usage data returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
