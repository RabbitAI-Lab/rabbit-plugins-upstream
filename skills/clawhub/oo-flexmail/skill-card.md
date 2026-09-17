## Description:

Flexmail (flexmail.be) lets an agent read, create, update, and delete Flexmail contacts, interests, subscriptions, preferences, and account metadata through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Flexmail through the oo CLI with an OOMOL-connected account, including contact management, interest and preference subscriptions, and account metadata lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags review need because first-time setup can run a remote installer directly on the user's machine.

Mitigation: Prefer an official, versioned oo CLI installation method with checksum or signature verification before using the skill.

Risk: Flexmail write and destructive actions can create, update, unsubscribe, or delete account data.

Mitigation: Inspect the live action schema, confirm exact target and payload with the user, and require explicit approval before running tagged write or destructive actions.

## Reference(s):

- [ClawHub Flexmail Skill Listing](https://clawhub.ai/oomol/skills/oo-flexmail)
- [Flexmail Homepage](https://flexmail.be/en)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema before payload construction; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
