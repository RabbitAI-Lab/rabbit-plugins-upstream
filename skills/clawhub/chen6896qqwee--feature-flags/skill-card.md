## Description: <br>
Remote feature flag and toggle system for AI agents, enabling features to be changed without redeploying. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add feature flags, rollout controls, A/B tests, and kill switches to AI-agent workflows without redeploying code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote flag polling can silently change agent feature behavior when pointed at a user-supplied endpoint without authentication or integrity checks. <br>
Mitigation: Use only trusted HTTPS flag endpoints, add endpoint authentication and response validation, and keep change logs for any remote flag updates. <br>
Risk: Untrusted users controlling --poll-url, --load, or --save values can influence flag behavior or local flag files. <br>
Mitigation: Restrict those arguments to trusted operators and trusted local paths before using the skill in sensitive workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chen6896qqwee/skills/feature-flags) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; reads and writes local JSON flag files and can poll a configured HTTP endpoint.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
