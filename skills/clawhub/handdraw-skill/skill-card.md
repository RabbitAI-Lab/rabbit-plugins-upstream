## Description: <br>
Create deterministic hand-drawn, whiteboard, educational, and explainer MP4 animations from a JSON Animation DSL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to turn a requested hand-drawn, whiteboard, educational, or explainer animation into a validated JSON project and rendered MP4 using local SVG assets. It supports optional narration when remote Edge TTS processing is acceptable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional narration sends narration text to the Edge TTS service for remote processing. <br>
Mitigation: Avoid private or regulated narration text unless remote processing is acceptable, or render without narration. <br>
Risk: Untrusted SVG assets or third-party project files may introduce unsafe or unwanted rendering behavior. <br>
Mitigation: Use trusted local SVG assets and review third-party project files and SVGs before validating or rendering. <br>
Risk: The skill depends on npm and Python packages plus FFmpeg in the runtime environment. <br>
Mitigation: Run the environment check before use and install dependencies only in trusted environments. <br>


## Reference(s): <br>
- [HandDraw Skill](artifact/SKILL.md) <br>
- [Animation DSL v1](artifact/references/dsl.md) <br>
- [Installing HandDraw Skill in Other Agents](artifact/references/agent-installation.md) <br>
- [Narrative character system](artifact/references/narrative-character-system.md) <br>
- [ClawHub skill page](https://clawhub.ai/tobewin/skills/handdraw-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with JSON project files and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces validated JSON Animation DSL projects and MP4 render commands; optional narration uses Edge TTS and FFmpeg.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
