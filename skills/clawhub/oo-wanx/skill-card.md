## Description:

Wanx helps agents inspect Wanx connector schemas and run image generation, video submission, and video retrieval actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to generate or edit Wanx images, submit Wan 3.0 video generation tasks, and retrieve video task state or output through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup guidance could execute arbitrary code if the installer source is compromised or not reviewed.

Mitigation: Review the installer path before installing, prefer a trusted and versioned installation method with integrity checks, and do not let an agent run the remote installer automatically.

Risk: Wanx actions that create or submit generated content can incur account-side effects or costs.

Mitigation: Confirm the exact payload and expected effect before running write actions such as video task submission or content generation.

## Reference(s):

- [Wanx homepage](https://tongyi.aliyun.com/wanxiang/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wanx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
