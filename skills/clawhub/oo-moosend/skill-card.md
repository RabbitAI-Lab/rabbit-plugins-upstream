## Description:

Moosend enables agents to read, create, and update Moosend account data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Moosend mailing lists and subscribers from an agent, including listing mailing lists, filtering subscribers, retrieving subscribers by email, and adding or updating subscribers after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes direct execution of a remote oo CLI installer.

Mitigation: Install the oo CLI from a verified, versioned source before using the skill.

Risk: Write actions can add or update Moosend subscriber records.

Mitigation: Review the exact subscriber payload and intended effect with the user before approving write operations.

Risk: Moosend actions are mediated through OOMOL-connected credentials.

Mitigation: Install only when the user is comfortable using OOMOL as the intermediary for Moosend actions.

## Reference(s):

- [Moosend homepage](https://www.moosend.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Moosend skill page](https://clawhub.ai/oomol/skills/oo-moosend)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that read Moosend data or, after user confirmation, write subscriber changes.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
