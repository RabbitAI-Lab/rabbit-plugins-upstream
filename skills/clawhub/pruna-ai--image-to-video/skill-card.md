## Description: <br>
Use when someone wants one short film beat from images - a narrated scene, story moment, or cinematic B-roll with optional voiceover. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to guide an agent through a single-scene image-to-video workflow with optional narration, review gates, and media generation handoffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can upload user images, audio, or generated media to external generation services. <br>
Mitigation: Use the documented data-handling gate before uploads or paid calls, and confirm that the user intends to send the media to those services. <br>
Risk: The workflow can trigger paid media generation calls. <br>
Mitigation: Require explicit approval at the plan, stills, and clip gates before running the paid video step. <br>
Risk: Requests for longer films or multi-scene outputs can exceed the skill boundary. <br>
Mitigation: Keep the workflow to one scene and one video job, or hand off to the related multi-scene or transition-reel skills. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated media artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses staged approval gates for plan, stills, TTS, video clip, and optional background music.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
