## Description: <br>
Checks whether a configured local ComfyUI health endpoint is reachable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xtopher86](https://clawhub.ai/user/xtopher86) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and ComfyUI users use this skill to check the reachability of a configured local ComfyUI instance from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documentation describes run, stop, and basic-auth behavior that is not implemented in this release. <br>
Mitigation: Use the skill only for status health checks, and do not rely on run, stop, or basic-auth behavior unless a future reviewed version implements it. <br>
Risk: The skill sends an HTTP health request to the configured ComfyUI host and port. <br>
Mitigation: Set COMFYUI_HOST and COMFYUI_PORT only to a trusted ComfyUI instance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xtopher86/skills/comfyui-runner) <br>
- [Publisher profile](https://clawhub.ai/user/xtopher86) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration] <br>
**Output Format:** [JSON status object] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and a reachable ComfyUI HTTP endpoint; only the status action is implemented in this release.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; package.json reports 0.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
