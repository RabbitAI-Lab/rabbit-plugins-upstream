## Description:

Doubao Seedream helps agents generate or edit images through an OOMOL-connected Doubao Seedream account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to generate or edit images with Doubao Seedream through an OOMOL-connected account. The skill guides the agent to inspect the live connector schema before constructing a request payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified official package or documented manual installation path, and review installer commands before execution.

Risk: Image-generation prompts, source images, or retries may consume credits or process user-provided content.

Mitigation: Confirm prompts, source images, and credit-consuming actions with the user before running generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-doubao-seedream)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Doubao Seedream homepage](https://www.volcengine.com/product/ark)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text, images]

**Output Format:** [Markdown with inline shell commands and JSON connector responses; image results are returned by the connector.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects the agent to inspect the live action schema before running generate_image.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
