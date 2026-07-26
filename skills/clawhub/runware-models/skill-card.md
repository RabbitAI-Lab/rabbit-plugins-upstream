## Description: <br>
Pick the right Runware model for a task and keep that choice current. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to choose, verify, and refresh Runware model selections for a requested capability, modality, status, and price target. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Runware catalog entries can change, causing a previously recommended model to be deprecated, unavailable, or mismatched to the requested capability. <br>
Mitigation: Perform a live catalog lookup before execution and prefer models with live status that explicitly list the required capability. <br>
Risk: Using related Runware tooling can consume a configured Runware account and incur provider costs. <br>
Mitigation: Check model pricing or dry-run the request before batch or high-volume execution. <br>


## Reference(s): <br>
- [Runware Models on ClawHub](https://clawhub.ai/runware/skills/runware-models) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable output; recommendations should be confirmed against the live Runware catalog before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
