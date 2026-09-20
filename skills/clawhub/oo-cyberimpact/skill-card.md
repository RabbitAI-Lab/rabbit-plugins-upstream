## Description:

Cyberimpact connector helper for reading, creating, updating, and deleting Cyberimpact data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Cyberimpact groups, members, and email templates through an OOMOL-connected account. It supports read, write, and destructive account actions, with live schema inspection before payload construction and confirmation before write or destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, replace, or delete Cyberimpact groups, members, and templates.

Mitigation: Inspect the live action schema, confirm the exact target and payload with the user, and require explicit approval before write or destructive actions.

Risk: The skill depends on an OOMOL-connected account to mediate Cyberimpact actions.

Mitigation: Confirm the user is comfortable with OOMOL mediating account actions before installation or use.

Risk: The fallback setup path includes pipe-to-shell CLI installation commands.

Mitigation: Verify the oo CLI installation source and prefer reviewed installation steps before running install commands.

## Reference(s):

- [Cyberimpact homepage](https://www.cyberimpact.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cyberimpact)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
