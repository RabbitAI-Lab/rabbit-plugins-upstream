## Description:

Personal AI (personal.ai) lets an agent read, create, and update Personal AI data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Personal AI personas through an OOMOL-connected account, including sending messages or instructions and uploading memories, text documents, or public URL content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions execute remote installer scripts for the oo CLI.

Mitigation: Review the installer workflow before installing and prefer a versioned, signed, or checksum-verified source.

Risk: Write actions can change Personal AI account state by sending messages, instructions, memories, documents, or URLs.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-personal-ai)
- [Personal AI Homepage](https://personal.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
