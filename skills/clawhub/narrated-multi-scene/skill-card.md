## Description: <br>
Use when someone wants a multi-part story with voiceover: episodic B-roll, chaptered promo, or several linked video scenes without on-camera dialogue. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to plan, gate, generate, review, and assemble narrated multi-scene videos from stills, TTS voiceover, video clips, optional music beds, and ffmpeg assembly steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can send prompts and media to external image, audio, and video generation services and may spend generation credits. <br>
Mitigation: Use the approval gates before generation, confirm media is appropriate to upload, and verify related skill installs come from the intended PrunaAI source. <br>
Risk: Narration-led video clips can be truncated or require regeneration when scene audio exceeds the documented duration limit. <br>
Mitigation: Check each narration file with ffprobe and keep scene lines at or below the skill's approximately 19 second gate before video generation. <br>
Risk: Generated stills, clips, or narration may not match the intended story, style, or continuity. <br>
Mitigation: Review the plan, stills, and clips at the required phase gates and rerun only the affected scene when corrections are needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/narrated-multi-scene) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with tables, JSON payload examples, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include scene plans, prompts, asset URLs, API payloads, ffmpeg commands, and assembly manifests.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
