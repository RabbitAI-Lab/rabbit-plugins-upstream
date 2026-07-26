## Description: <br>
Onboard and operate SoundClaw through one thin OpenClaw-facing product and the promoted runtime CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[catholicbeer](https://clawhub.ai/user/catholicbeer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and developers use this skill to check SoundClaw readiness and route supported playback, volume, output, zone, scene, layer, health, configuration, deployment identity, and ingest requests through the documented local runtime CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local soundclawctl commands that affect playback, volume, outputs, zones, scenes, and library ingest. <br>
Mitigation: Use it only with an intended SoundClaw backend, clarify targets before mutating commands, and rely on runtime-owned command results. <br>
Risk: Backend installation, repair, update, rollback, and service manipulation are outside the skill boundary. <br>
Mitigation: Stop before host mutation when the backend is missing or unhealthy and direct operators to the documented public release bundle workflow. <br>


## Reference(s): <br>
- [SoundClaw operator reference](references/README.md) <br>
- [SoundClaw examples](references/examples.md) <br>
- [SoundClaw compatibility](references/compatibility.md) <br>
- [SoundClaw public release bundles](https://github.com/catholicbeer/soundclaw-release/releases) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands and concise runtime-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local soundclawctl command results as authoritative runtime evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
