## Description:

Enables agents to search and read Contentstack Content Delivery data through OOMOL's oo CLI and connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve Contentstack content type schemas, published entries, and published assets through an OOMOL-connected Contentstack account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI through a verified official method, inspect installer contents before execution, and do not let an agent run those installer commands automatically.

Risk: The skill depends on an OOMOL-connected Contentstack account and may prompt authentication, connection, or billing actions when commands fail.

Mitigation: Keep OOMOL sign-in, Contentstack connection setup, scope changes, credential refresh, and billing actions under explicit user control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-contentstack-content-delivery)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Contentstack Content Delivery homepage](https://www.contentstack.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide the agent to inspect live connector schemas and run read-oriented Contentstack actions through the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
