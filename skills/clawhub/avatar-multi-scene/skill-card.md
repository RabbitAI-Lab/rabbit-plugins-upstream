## Description: <br>
Use when someone wants the same person hosting several clips - multi-segment UGC, comparison reels, or mixed speaking and animated scenes with continuity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agent operators use this skill to plan and produce coherent multi-scene avatar reels that keep a host or persona consistent across speaking clips, animated motion-transfer beats, slider comparisons, and final ffmpeg assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Portraits, reference videos, scripts, and generated media may be uploaded to Pruna services. <br>
Mitigation: Use rights-cleared media and review the scene plan and stills before approving uploads or generation. <br>
Risk: Approved generation can spend Pruna API credits. <br>
Mitigation: Keep the plan, stills, and clips approval gates; do not start paid predictions before explicit approval. <br>
Risk: PRUNA_API_KEY exposure could grant access to Pruna API usage. <br>
Mitigation: Keep PRUNA_API_KEY scoped and private, and do not include it in prompts, logs, or shared artifacts. <br>
Risk: Poor pose, framing, or proportion alignment can produce broken motion-transfer clips. <br>
Mitigation: Match shot size, facing direction, and limb visibility; repose with p-image-edit or choose a closer motion template before p-video-animate. <br>


## Reference(s): <br>
- [Avatar Multi Scene on ClawHub](https://clawhub.ai/pruna-ai/skills/avatar-multi-scene) <br>
- [Prompt templates](prompt-templates.md) <br>
- [Animate beats](animate-beats.md) <br>
- [Examples](examples.md) <br>
- [Batch template](templates/batch.template.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON snippets, API request fields, and ffmpeg shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce scene plans, cast ledgers, prompt fields, batch manifests, approval checkpoints, and local assembly commands.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
