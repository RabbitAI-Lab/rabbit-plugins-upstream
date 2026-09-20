## Description:

Metaso lets an agent use OOMOL's oo CLI to search Metaso content, read webpages, and create Metaso chat completions through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Metaso through an OOMOL-connected account: search webpages, documents, papers, images, videos, and podcasts; read webpages; and request grounded chat completions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup section includes shell commands that execute remote installer scripts directly.

Mitigation: Do not let an agent run those install commands automatically; review official, version-pinned oo CLI installation instructions and verify checksums or signatures before installing.

Risk: The Metaso streaming chat completion action is tagged as a write action and may change service-side state.

Mitigation: Confirm the exact payload and expected effect with the user before running tagged write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-metaso)
- [Metaso homepage](https://metaso.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
