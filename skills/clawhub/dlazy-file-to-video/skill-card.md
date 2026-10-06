## Description:

Helps turn PPT, Word, Excel, and PDF documents into narrated explainer, report, courseware, or training videos through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business users can provide documents and request narrated explainer, report, courseware, or training videos, then continue work across project sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's cloud service.

Mitigation: Attach only files you intend to upload and review their contents before sending.

Risk: The CLI may save a dLazy API key locally, and global installation adds a persistent binary.

Mitigation: Review the pinned CLI package before installation; use npx or a per-run DLAZY_API_KEY when persistence is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped, multi-turn responses; the hosted service handles video generation.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
