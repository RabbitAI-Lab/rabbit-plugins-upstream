## Description:

Jungle Scout lets agents search and read Amazon product, keyword, sales-estimate, and share-of-voice data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketplace operators, and ecommerce analysts use this skill to query Jungle Scout product research, keyword research, sales estimate, and brand share-of-voice data from an OOMOL-connected Jungle Scout account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time installer can execute a remote installation script for the oo CLI.

Mitigation: Review the installer before running it, or use OOMOL's official installation guidance before proceeding.

Risk: Jungle Scout credentials are handled server-side by OOMOL.

Mitigation: Install and use the skill only if you trust OOMOL to broker Jungle Scout access for the connected account.

## Reference(s):

- [Jungle Scout ClawHub skill page](https://clawhub.ai/oomol/skills/oo-junglescout)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Jungle Scout homepage](https://www.junglescout.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return JSON-shaped connector responses containing data and execution metadata when the agent runs oo CLI actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
