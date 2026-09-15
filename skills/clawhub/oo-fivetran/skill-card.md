## Description:

This skill helps agents operate Fivetran through an OOMOL-connected account by inspecting connector schemas and running documented connector actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Fivetran connector schemas and run OOMOL-connected Fivetran read actions for hybrid deployment agents, log services, and transformation projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fivetran request and response data passes through OOMOL when the skill runs connector actions.

Mitigation: Use the skill only when this third-party data path is acceptable for the target Fivetran account and data.

Risk: The skill includes remote installer commands for the oo CLI.

Mitigation: Avoid running remote installer commands unless the installation source has been independently trusted and verified.

Risk: Connector actions outside the documented read-oriented set may change Fivetran state.

Mitigation: Prefer the documented read-only actions and separately confirm any write-capable action and exact payload before execution.

## Reference(s):

- [Fivetran homepage](https://fivetran.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fivetran)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; documented actions are read-oriented.]

## Skill Version(s):

1.0.2 (source: server evidence release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
