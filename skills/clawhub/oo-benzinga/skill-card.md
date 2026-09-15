## Description:

Benzinga (benzinga.com) lets agents search and retrieve Benzinga data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Benzinga market data, including consensus ratings, analyst ratings, earnings calendar entries, and news channels, through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that first-time setup documents remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the skill before installing it, install the oo CLI through a verified and reviewable method under normal user privileges, and do not allow an agent to run the pipe-to-shell installer automatically.

Risk: The skill depends on OOMOL-mediated Benzinga access and server-side credentials.

Mitigation: Use the skill only with an intended OOMOL account and confirm authentication, app connection, and billing steps manually when required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-benzinga)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Benzinga Homepage](https://www.benzinga.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect the live connector schema before constructing JSON payloads and to return connector responses that include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
