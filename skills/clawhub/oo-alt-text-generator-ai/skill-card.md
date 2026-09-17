## Description:

Generates concise, accessibility-friendly alt text for publicly reachable image URLs through an OOMOL-connected Alt Text Generator AI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to request alt text for images by providing a public image URL through an agent connected to their OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may encourage running unverified remote installer scripts directly in a shell.

Mitigation: Prefer an official package manager or downloaded installer with checksum or signature verification, and avoid elevated shells during installation.

Risk: Connected-account operations could be run with an unintended action or payload.

Mitigation: Inspect the live connector schema before each action run and confirm the exact action and payload before using account-connected operations.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-alt-text-generator-ai)
- [Alt Text Generator AI homepage](https://alttextgeneratorai.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash and JSON command examples; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces alt text for publicly reachable image URLs; action payloads should follow the live connector schema.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
