## Description:

Mailcoach lets an agent manage Mailcoach email lists and subscribers through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Mailcoach users and operators use this skill to list, inspect, create, update, subscribe, unsubscribe, and delete Mailcoach email list and subscriber records from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change subscriber or email list state.

Mitigation: Confirm the exact payload and intended effect with the user before running actions tagged as write.

Risk: Destructive actions can delete records, unsubscribe subscribers, or otherwise remove access to Mailcoach data.

Mitigation: Confirm the target identifier and get explicit approval before running delete or unsubscribe actions.

Risk: The setup path may install or invoke the oo CLI on a user's machine.

Mitigation: Review the oo CLI install step before allowing it on a new machine and only use setup commands after an auth or connection failure.

## Reference(s):

- [ClawHub Mailcoach Skill](https://clawhub.ai/oomol/skills/oo-mailcoach)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Mailcoach Connection](https://console.oomol.com/app-connections?provider=mailcoach)
- [Mailcoach Homepage](https://www.mailcoach.app)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON request payloads and responses from Mailcoach connector actions.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
