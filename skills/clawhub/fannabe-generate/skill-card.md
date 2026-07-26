## Description: <br>
Generate images, videos, and voice for your AI models via Fannabe. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fannabe](https://clawhub.ai/user/fannabe) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to direct an agent through Fannabe CLI workflows for generating, editing, animating, captioning, and downloading Fannabe media with their signed-in account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands use the signed-in Fannabe CLI session and generation can spend Fannabe credits. <br>
Mitigation: Review billable requests before running them, preview costs with `fannabe generate cost` when useful, and surface estimated cost before non-trivial generation. <br>
Risk: Gallery and download commands may expose private account media. <br>
Mitigation: Use account-reading or download commands only for explicit Fannabe tasks and keep downloaded media in user-approved locations. <br>


## Reference(s): <br>
- [Fannabe](https://www.fannabe.com) <br>
- [Fannabe Generate on ClawHub](https://clawhub.ai/fannabe/skills/fannabe-generate) <br>
- [Choosing an AI](references/ai.md) <br>
- [Easy mode: Theme and Outfit presets](references/easy-mode.md) <br>
- [Source media: image-to-video, edits, motion control, character swap](references/source-media.md) <br>
- [Prompt assistance](references/prompt-tools.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Fannabe CLI commands that spend credits, inspect account gallery media, or download generated files when the user asks.] <br>

## Skill Version(s): <br>
0.1.5 (source: evidence release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
