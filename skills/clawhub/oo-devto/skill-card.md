## Description:

Dev.to enables agents to read Dev.to articles and user, organization, tag, and video data, and to create or update articles through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Dev.to account from an agent workflow. It supports reading Dev.to resources, inspecting action schemas, and creating or updating articles after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to execute remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation method before installing; prefer official, versioned, verifiable installers or inspect downloaded scripts before execution.

Risk: Create and update actions can change public Dev.to content.

Mitigation: Confirm the exact create_article or update_article payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-devto)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Dev.to Homepage](https://dev.to)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include action-schema inspection steps and confirmation prompts before write actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
