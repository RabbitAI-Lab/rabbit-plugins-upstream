## Description: <br>
Security scanner for ClawHub skills from Gen Digital that looks up skill safety via the scan API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rexshang](https://clawhub.ai/user/rexshang) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to check a ClawHub skill URL with Gen Digital's scanner before deciding whether to install or use that skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided ClawHub skill URLs to Gen Digital's external scanner API. <br>
Mitigation: Use it only for public or approved skill URLs, avoid private or access-controlled URLs unless the service is intended to receive them, and treat scanner results as one review input. <br>
Risk: A clean or safe scanner result is not a complete security guarantee. <br>
Mitigation: Combine the result with sandboxing, least privilege, ClawScan evidence, and manual review before relying on a skill. <br>


## Reference(s): <br>
- [ClawHub Skillscanner listing](https://clawhub.ai/rexshang/skills/skillscanner) <br>
- [Agent Trust Hub](https://ai.gendigital.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON response interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scanner results should be treated as advisory and reviewed before relying on security conclusions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
