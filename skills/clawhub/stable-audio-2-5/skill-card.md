## Description: <br>
Use when someone wants light instrumental background music -- an ambient bed under dialogue or underscore for reels and explainers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agent operators use this skill to generate light instrumental background music through Replicate's Stable Audio 2.5 model for reels, explainers, and dialogue beds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill requires a Replicate API token and may incur Replicate usage costs. <br>
Mitigation: Confirm REPLICATE_API_TOKEN is available, keep it out of prompts and logs, and run generation only after the user accepts possible provider costs. <br>
Risk: The skill delegates prompt-crafting and API-handling guidance to prerequisite Pruna skills. <br>
Mitigation: Review and load the referenced prerequisite skills before making paid API calls or generating audio. <br>
Risk: The audio mix step depends on ffmpeg and ffprobe being installed on PATH. <br>
Mitigation: Check tool availability before attempting the mix step and stop with setup guidance if either dependency is missing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/stable-audio-2-5) <br>
- [Replicate Stable Audio 2.5 prediction endpoint](https://api.replicate.com/v1/models/stability-ai/stable-audio-2.5/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline bash and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides a Replicate prediction request, polling, MP3 download, and optional audio mix preparation.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
