## Description:

Yelp lets an agent search Yelp businesses and retrieve business details through the OOMOL Yelp connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Yelp businesses by keyword, location, or phone number and retrieve business details through an OOMOL-connected Yelp account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands that execute downloaded scripts directly.

Mitigation: Review the installer before use or replace it with a pinned and verifiable CLI installation path.

Risk: Yelp queries are routed through an OOMOL-connected account.

Mitigation: Confirm the user intends to use OOMOL for Yelp access and that the connected account, scopes, and billing status are appropriate before retrying setup or connection failures.

## Reference(s):

- [ClawHub Yelp skill](https://clawhub.ai/oomol/skills/oo-yelp)
- [Yelp homepage](https://www.yelp.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash and PowerShell command examples; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Yelp action schemas before connector calls and returns execution metadata when actions run.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
