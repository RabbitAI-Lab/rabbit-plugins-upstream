## Description:

Use this skill for Rootly requests that search and read Rootly data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Rootly connector schemas and retrieve Rootly users, incidents, services, and teams through an authenticated OOMOL CLI connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on broad authenticated OOMOL CLI access for Rootly operations.

Mitigation: Install only when the user is comfortable with the agent using the authenticated OOMOL CLI, and review proposed oo commands before execution.

Risk: The first-time setup guidance includes remote installer commands.

Mitigation: Prefer manual installation from verified official instructions before allowing an agent to run installer commands.

## Reference(s):

- [ClawHub Rootly Skill](https://clawhub.ai/oomol/skills/oo-rootly)
- [Rootly Homepage](https://rootly.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rootly connector responses are JSON objects returned by the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
