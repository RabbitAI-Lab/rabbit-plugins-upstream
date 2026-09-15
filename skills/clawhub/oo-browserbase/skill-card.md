## Description:

Operate Browserbase through an OOMOL-connected account using the oo CLI for reading, creating, updating, and deleting Browserbase resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Browserbase action schemas and run Browserbase connector actions for sessions, contexts, projects, and usage through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use a verified, pinned, official installation method where possible instead of running pipe-to-shell installers as written.

Risk: The skill can run write and destructive Browserbase actions through the OOMOL oo CLI.

Mitigation: Confirm the exact payload, target resource, and expected effect before allowing write or destructive actions.

Risk: Browserbase actions are routed through OOMOL's oo CLI and connected account flow.

Mitigation: Install and use the skill only when that routing model is acceptable for the deployment.

## Reference(s):

- [Browserbase homepage](https://www.browserbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-browserbase)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that return JSON responses from Browserbase connector actions.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
