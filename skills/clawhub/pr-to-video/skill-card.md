## Description: <br>
Turn a GitHub pull request into a code-change explainer video using the PR diff, commits, and files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to convert a GitHub pull request into a storyboarded, narrated HyperFrames explainer video for changelogs, feature reveals, fixes, or refactor walkthroughs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may update globally installed HyperFrames skills without asking first. <br>
Mitigation: Review and approve this update behavior before installation, and run the skill only where global skill changes are acceptable. <br>
Risk: The skill uses GitHub CLI access to read PR metadata and diffs and may contact media services for audio or assets. <br>
Mitigation: Use it only with repositories, credentials, and media-service access that are approved for the task. <br>


## Reference(s): <br>
- [Skill source](artifact/SKILL.md) <br>
- [Story design reference](artifact/references/story-design.md) <br>
- [Visual design reference](artifact/references/visual-design.md) <br>
- [Code vocabulary reference](artifact/references/code-vocabulary.md) <br>
- [Motion language reference](artifact/references/motion-language.md) <br>
- [Cut catalog reference](artifact/references/cut-catalog.md) <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/pr-to-video) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, video] <br>
**Output Format:** [Markdown guidance, shell commands, project files, HTML frame compositions, and rendered MP4 output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses GitHub PR metadata and diffs as source material; may generate narration, captions, contributor avatar assets, and HyperFrames project artifacts.] <br>

## Skill Version(s): <br>
1.0.20 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
