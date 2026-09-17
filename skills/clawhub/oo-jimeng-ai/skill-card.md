## Description:

Jimeng AI connector skill for using an OOMOL-connected account to submit and retrieve image generation, text-to-image, video generation, smart upscale, and Lilinque video agent tasks through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Jimeng AI connector schemas, submit supported media generation and upscaling jobs, and retrieve asynchronous results through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review installation commands before use and prefer verified, pinned, or signed oo CLI release instructions.

Risk: Write actions can submit Jimeng AI generation or upscaling jobs that change account state or consume credits.

Mitigation: Confirm the exact action, payload, expected effect, and account credit impact with the user before running write actions.

## Reference(s):

- [Jimeng AI Skill Page](https://clawhub.ai/oomol/skills/oo-jimeng-ai)
- [Jimeng AI Homepage](https://www.volcengine.com/product/jimeng)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async actions return execution metadata for later result retrieval.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
