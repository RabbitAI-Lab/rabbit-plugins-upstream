## Description: <br>
Agentvibes Skill helps agents guide enterprise text-to-speech workflows for neural voices, multi-role narration, batch audio export, background music, and audio effects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, enterprise content teams, game teams, and customer-support teams use this skill to configure and run professional TTS production workflows such as audiobook, podcast, IVR, and character-dialogue audio generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may run local audio tools and write exported audio files. <br>
Mitigation: Review proposed commands before execution and choose explicit output directories with appropriate file permissions. <br>
Risk: The workflow uses the AGENTVIBES_LICENSE environment variable for professional features. <br>
Mitigation: Store the license in a secret manager or local environment configuration and avoid committing it to scripts, logs, or shared shell history. <br>
Risk: The workflow may retrieve TTS dependencies such as Piper before execution. <br>
Mitigation: Confirm the download source and package integrity before allowing dependency installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agentvibes-skill) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with command examples and JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create audio files in user-selected output directories when the agent executes the described TTS workflow.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
