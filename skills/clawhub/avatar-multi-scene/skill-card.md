## Description: <br>
Use when someone wants the same person hosting several clips - multi-segment UGC, comparison reels, or mixed speaking and animated scenes with continuity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and agent operators use this skill to plan and produce coherent multi-scene avatar or motion-transfer reels with a recurring host or character. It guides intake, continuity planning, staged approvals, Pruna image/video generation, and ffmpeg assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can install related Pruna skills and use a Pruna API key. <br>
Mitigation: Review the required skills and confirm the API key scope before allowing generation. <br>
Risk: The workflow can upload user-provided media and spend generation credits. <br>
Mitigation: Confirm media rights and require the documented approval gates before any paid generation. <br>
Risk: Poorly matched motion templates and reference images can produce visible artifacts in animate rows. <br>
Mitigation: Use the documented alignment checks, repose with p-image-edit when needed, and review stills before video generation. <br>
Risk: The workflow can run local ffmpeg commands for sliders and assembly. <br>
Mitigation: Review generated shell commands and file paths before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/avatar-multi-scene) <br>
- [Prompt templates](prompt-templates.md) <br>
- [Animate beats](animate-beats.md) <br>
- [Examples](examples.md) <br>
- [Batch template](templates/batch.template.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with JSON manifest patterns and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses staged approval gates before paid generation, PRUNA_API_KEY for Pruna calls, and local ffmpeg commands for comparison clips and final assembly.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
