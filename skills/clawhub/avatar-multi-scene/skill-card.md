## Description: <br>
Use when someone wants the same person hosting several clips -- multi-segment UGC, comparison reels, or mixed speaking and animated scenes with continuity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to plan and generate coherent multi-scene avatar reels with recurring hosts, avatar speaking clips, motion-transfer segments, comparison renders, and final ffmpeg assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected reference media may be uploaded to Pruna services during the workflow. <br>
Mitigation: Confirm media rights and user approval before uploads, and record approved source files in the project manifest. <br>
Risk: Generation calls can use PRUNA_API_KEY and may consume paid API credits. <br>
Mitigation: Keep the API key in the environment, avoid exposing it in prompts or logs, and require the documented approve plan, approve stills, and approve clips gates before paid video generation. <br>
Risk: Local ffmpeg assembly commands process generated and uploaded media files. <br>
Mitigation: Review command paths and clip order before execution, and use the skill's staged manifest to track inputs, outputs, and failed attempts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/avatar-multi-scene) <br>
- [Animate beats](artifact/animate-beats.md) <br>
- [Prompt templates](artifact/prompt-templates.md) <br>
- [Examples](artifact/examples.md) <br>
- [Batch template](artifact/templates/batch.template.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON snippets and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides staged generation, records scene manifests, and proposes ffmpeg commands for local video assembly.] <br>

## Skill Version(s): <br>
1.0.8 (source: server evidence release.version and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
