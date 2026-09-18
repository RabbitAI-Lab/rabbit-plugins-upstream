## Description:

Operate Doubao Seedream through OOMOL's oo CLI to generate or edit images with an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect the live Doubao Seedream connector schema and run image generation or image editing actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented generate_image action may create or edit outputs and consume service credits.

Mitigation: Confirm the exact action payload and expected effect with the user before running the action.

Risk: The skill includes remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Use a verified, pinned installation path from a trusted source instead of executing remote installer scripts directly.

Risk: The frontmatter describes the skill as search/read oriented even though the available action is image generation or editing.

Mitigation: Treat the skill as image generation/editing guidance and inspect the live connector schema before constructing payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-doubao-seedream)
- [Doubao Seedream homepage](https://www.volcengine.com/product/ark)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Images, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated or edited image outputs are produced by the connected Doubao Seedream service; command responses include execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
