## Description: <br>
Monitors Anti-Gravity model quotas and switches OpenClaw's default model to the model with the most remaining quota, falling back to gemini-flash below the configured threshold. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sarielwang93](https://clawhub.ai/user/sarielwang93) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators who use OpenClaw can run this skill manually or on a schedule to keep the default model aligned with available Anti-Gravity quota and fall back when quota is low. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic scheduling can change OpenClaw's default model without an operator reviewing each switch. <br>
Mitigation: Install or schedule this skill only where automatic model switching is intended, and review the candidate model list, threshold, and fallback model before unattended use. <br>
Risk: Some Gemini Anti-Gravity models are treated as full quota when not reported by model status. <br>
Mitigation: Confirm that this quota assumption matches the target OpenClaw environment before relying on the skill for production routing decisions. <br>


## Reference(s): <br>
- [Model Guard ClawHub skill page](https://clawhub.ai/sarielwang93/skills/model-guard) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [CLI output text and OpenClaw model configuration changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May change OpenClaw's default model according to quota status, candidate model list, threshold, and fallback settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
