## Description:

Readwise connector for reading, creating, and updating Readwise and Readwise Reader data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Readwise through an OOMOL-connected account, including highlight creation, highlight export, book/source listing, Reader document listing, URL saving, and document updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may execute unverified remote installer scripts from OOMOL endpoints.

Mitigation: Review the installer before execution or use a verified, pinned package source.

Risk: Write actions can create highlights, save URLs, or update Readwise Reader documents.

Mitigation: Confirm the exact action payload and expected effect with the user before allowing write execution.

## Reference(s):

- [ClawHub Readwise skill page](https://clawhub.ai/oomol/skills/oo-readwise)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Readwise homepage](https://readwise.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; Readwise write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
