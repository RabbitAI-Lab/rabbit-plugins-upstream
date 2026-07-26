## Description: <br>
Security check for ClawHub skills powered by Koi. Query the Clawdex API before installing any skill to verify it's safe. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wearekoi](https://clawhub.ai/user/wearekoi) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to check ClawHub skills against Koi's Clawdex API before installation and to review already installed skills for advisory security verdicts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Candidate or installed skill names may be sent to Koi's Clawdex API during checks. <br>
Mitigation: Use the skill only when this disclosure is acceptable for the workspace. <br>
Risk: Clawdex verdicts are advisory and may be unknown or incomplete. <br>
Mitigation: Keep user approval in the loop and review unknown or risky skills before installation. <br>


## Reference(s): <br>
- [Clawdex by Koi on ClawHub](https://clawhub.ai/wearekoi/skills/clawdex) <br>
- [Koi](https://www.koi.ai/) <br>
- [Clawdex API endpoint pattern](https://clawdex.koi.security/api/skill/SKILL_NAME) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Verdicts are advisory; unknown or risky skills should remain subject to user review and approval.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
