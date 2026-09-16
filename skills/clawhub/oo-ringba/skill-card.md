## Description:

Ringba (ringba.com). Use this skill for ANY Ringba request - searching and reading data. Whenever a task involves Ringba, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve Ringba account, campaign, phone number, and publisher data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run an unverified internet installer directly in a shell.

Mitigation: Review the install method before use, prefer a verified or package-manager installation path for the OOMOL CLI, and avoid elevated shells.

Risk: The connected Ringba account may expose more data than the user needs for read-only work.

Mitigation: Connect Ringba with the least privileges needed and confirm account scope before retrieving account, campaign, phone number, or publisher data.

## Reference(s):

- [Ringba homepage](https://www.ringba.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ringba)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only Ringba connector actions unless future actions are explicitly tagged as write or destructive.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
