## Description:

SwaggerHub (swagger.io). Use this skill for ANY SwaggerHub request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and API teams use this skill to search SwaggerHub and retrieve API, domain, template, project, and version information through an OOMOL-connected SwaggerHub account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the oo CLI and an OOMOL-connected SwaggerHub account, which can carry local and account-level authority beyond simple read requests.

Mitigation: Install or update the CLI only from a verifiable official package or reviewed installer, and use the skill only when you trust OOMOL and the connected account context.

Risk: Broad command execution through the allowed oo CLI surface could be misused if an agent attempts actions beyond the listed read workflows.

Mitigation: Confirm the agent runs only documented get, list, and search actions unless you explicitly approve a broader command or payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-swaggerhub)
- [SwaggerHub homepage](https://swagger.io/tools/swaggerhub/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [Skill icon](https://static.oomol.com/logo/third-party/Swaggerhub.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return SwaggerHub connector data wrapped in JSON with execution metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
