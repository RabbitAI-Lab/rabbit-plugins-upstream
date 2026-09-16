## Description:

Leexi (leexi.ai). Use this skill for ANY Leexi request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Leexi action schemas and retrieve Leexi calls, meetings, call notes, teams, and users through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may run a remote installer directly in a shell.

Mitigation: Install the oo CLI from a verified official package or inspect the installer before running it.

Risk: Leexi read requests are routed through OOMOL-connected credentials.

Mitigation: Confirm the connected account and intended Leexi workspace before running connector actions.

## Reference(s):

- [ClawHub Leexi Skill](https://clawhub.ai/oomol/skills/oo-leexi)
- [Leexi Homepage](https://www.leexi.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from Leexi connector actions when commands are executed.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
