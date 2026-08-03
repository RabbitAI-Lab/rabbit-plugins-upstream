## Description: <br>
ACE音乐生成-专业版 guides agents through professional ACE Music workflows for text-to-music, batch generation, cover creation, repainting, long-duration output, and result handling for commercial music production. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, developers, and commercial content teams use this skill to configure and run ACE Music Pro workflows for advertising music, cover or repaint tasks, long-form scoring, and batch candidate generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an ACE Music Pro API key and may process user-supplied audio files through an external API. <br>
Mitigation: Use only task-specific audio inputs, store the API key in an environment variable or secret manager, and confirm that external API use is intended before running workflows. <br>
Risk: The artifact contains shell examples and output paths that an agent may adapt for local execution. <br>
Mitigation: Review generated commands and output destinations before execution, especially archive or file-move steps. <br>
Risk: Several examples reference a helper script that is not included in the artifact. <br>
Mitigation: Verify or supply the expected helper script before relying on the command examples as runnable workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ace-music-tool-pro) <br>
- [ACE Music API base URL](https://api.acemusic.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code] <br>
**Output Format:** [Markdown guidance with inline bash commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing workflow steps for external ACE Music Pro API usage; generated music files are produced by the external service or referenced helper commands, not by the skill text itself.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
