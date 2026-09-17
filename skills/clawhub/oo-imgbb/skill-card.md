## Description:

ImgBB enables agents to upload images to ImgBB through the OOMOL-connected oo CLI and return hosted image metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to inspect the ImgBB connector schema, construct valid JSON payloads, and upload images from public URLs or Base64 content through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute changing code from the internet.

Mitigation: Prefer an official signed or version-pinned installation path and inspect downloaded installer scripts before execution.

Risk: Image uploads create hosted ImgBB content and change remote service state.

Mitigation: Confirm the exact upload payload and expected effect with the user before running the upload action.

Risk: The skill depends on trust in OOMOL and the ImgBB connector.

Mitigation: Use the skill only with a trusted OOMOL account and inspect the live connector schema before constructing requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-imgbb)
- [ImgBB Homepage](https://imgbb.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL ImgBB Connection Settings](https://console.oomol.com/app-connections?provider=imgbb)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that return JSON responses containing hosted image metadata and execution IDs.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
