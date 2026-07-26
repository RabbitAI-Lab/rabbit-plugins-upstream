## Description: <br>
Enforces strict operational safety rules to prevent unauthorized system changes, unsafe network exposure, and protect core files and configurations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and workspace operators use this skill to apply strict OpenClaw operational safety guardrails, refuse unsafe system changes, and provide safer alternatives for risky requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Strict guardrails may refuse some direct administrative requests, including runtime updates, plugin removal, system configuration, webhook setup, broad installs, and workspace deletion. <br>
Mitigation: Install only when strict OpenClaw safety behavior is desired, and route owner-only or platform-level changes through supported official channels. <br>
Risk: Requests in group chat could attempt to expose protected identity, memory, credential, or configuration content. <br>
Mitigation: Keep task output scoped to the legitimate request and do not disclose protected file contents, enumerate system topology, or accept out-of-band authorization claims. <br>


## Reference(s): <br>
- [Worker Safety artifact](artifact/SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/worker-safety) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text] <br>
**Output Format:** [Markdown policy guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides refusal rules and safe-alternative guidance for OpenClaw operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
