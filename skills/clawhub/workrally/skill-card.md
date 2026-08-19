## Description:

WorkRally helps agents use the WorkRally CLI to create AIGC comic-drama videos, including image, video, audio, prompt optimization, project, series, shot, canvas, upload, download, asset, and material workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and content teams use this skill to guide an agent through WorkRally CLI workflows for AI media generation and managing projects, series, shots, canvases, uploads, and assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad authority to mutate cloud-side WorkRally resources.

Mitigation: Install only when agent operation of the WorkRally account is intended, and review uploads, downloads, deletes, canvas overwrites, and tool passthrough calls before execution.

Risk: Cross-scope recognition or all-library searches can affect resources beyond the intended project.

Mitigation: Keep recognition project-scoped by default and expand scope only after explicit confirmation.

Risk: Uploading sensitive local files sends them to WorkRally.

Mitigation: Avoid uploading sensitive files unless the user explicitly intends to send those files to WorkRally.

## Reference(s):

- [WorkRally homepage](https://workrally.qq.com)
- [WorkRally API key configuration](https://workrally.qq.com/open-api)
- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/workrally)
- [SkillHub listing](https://skillhub.cn/skills/workrally)
- [Skills listing](https://skills.sh/tencent/workrally/workrally)
- [AI generation guide](references/ai-generation-guide.md)
- [Canvas guide](references/canvas-guide.md)
- [Common pitfalls](references/common-pitfalls.md)
- [Shotlist guide](references/shotlist-guide.md)
- [Upload and assets guide](references/upload-and-assets-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce WorkRally JSON, text, or table output depending on CLI options.]

## Skill Version(s):

2.6.2 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
