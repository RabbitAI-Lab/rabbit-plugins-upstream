## Description:

DocuSeal connector for reading, creating, and updating DocuSeal data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect DocuSeal action schemas, list or retrieve templates, and create signature submissions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute changing remote installer code for the oo CLI.

Mitigation: Install the oo CLI from a versioned, verifiable source, or inspect and verify the downloaded installer before running it.

Risk: The create_submission action changes DocuSeal state by creating a signature request from an existing template.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [DocuSeal homepage](https://www.docuseal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docuseal)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live DocuSeal action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
