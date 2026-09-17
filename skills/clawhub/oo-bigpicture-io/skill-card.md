## Description:

BigPicture.io (bigpicture.io) supports searching and reading company data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to look up BigPicture.io company profiles by domain name or IP address through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute a remote installer on the user's machine.

Mitigation: Review and install the oo CLI through a verified or reviewed method instead of allowing an agent to run the remote installer automatically.

Risk: The skill depends on user authentication, a BigPicture.io connection, and available OOMOL credit.

Mitigation: Run setup or billing steps only after a command fails with the matching authentication, connection, scope, credential, app, or HTTP 402 error.

## Reference(s):

- [BigPicture.io homepage](https://bigpicture.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing requests.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
