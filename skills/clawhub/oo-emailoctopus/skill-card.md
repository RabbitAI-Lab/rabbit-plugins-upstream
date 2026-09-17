## Description:

EmailOctopus (emailoctopus.com). Use this skill for ANY EmailOctopus request - reading, creating, updating, and deleting data. Whenever a task involves EmailOctopus, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage EmailOctopus campaigns, mailing lists, and contacts through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can direct users to run remote oo CLI installer scripts without built-in verification.

Mitigation: Review the installer through a trusted channel and prefer signed or checksum-verified installation before use.

Risk: Write and destructive actions can create, update, or delete EmailOctopus contact data.

Mitigation: Confirm exact payloads and targets with the user before contact creation, update, or deletion.

## Reference(s):

- [EmailOctopus homepage](https://emailoctopus.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-emailoctopus)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live EmailOctopus action schemas before requests and may return JSON command output from the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
