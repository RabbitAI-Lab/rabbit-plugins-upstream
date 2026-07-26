## Description: <br>
Model Pyramid gives agents advisory rules for right-sizing delegated subagent model tiers and reasoning effort during fan-out. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Model Pyramid when spawning or delegating subagents to choose capability tiers and reasoning effort for peer work, exploration, large homogeneous lookup fan-outs, and default tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect sizing advice could affect agent cost, latency, or output quality. <br>
Mitigation: Review the per-subagent recommendation before applying it in a runtime, especially for production fan-outs. <br>
Risk: Runtime-specific model or effort knobs may not match the conceptual pyramid vocabulary. <br>
Mitigation: Use the runtime mapping reference and state any nearest-notch substitution or unsupported-knob degradation. <br>


## Reference(s): <br>
- [Runtime Mapping](references/runtime-mapping.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/vincentjiang06/skills/model-pyramid) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with optional shell command examples and per-subagent report lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory only; recommendations should be reviewed before applying to a runtime.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
