## Description: <br>
Locally scans OpenClaw and ClawHub skills for security risks such as hardcoded secrets, dangerous calls, risky imports, obfuscation, and hardcoded IP addresses, then reports risk scores and can quarantine threats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abyousef739](https://clawhub.ai/user/abyousef739) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, maintainers, and agents use this skill to scan local skill directories before installation or execution and review detected security risks. Quarantine should be used deliberately after confirming the target path and risk report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The quarantine feature moves local files and can overwrite an existing quarantine entry with the same base name. <br>
Mitigation: Use scan-only mode by default, verify the target path manually, and run quarantine only after confirming the reported high-risk directory. <br>
Risk: The artifact promotes autonomous quarantine behavior without enough safeguards. <br>
Mitigation: Do not allow agents to call quarantine automatically; require human or policy approval before file-moving actions. <br>


## Reference(s): <br>
- [ClawSkillShield ClawHub page](https://clawhub.ai/abyousef739/skills/clawskillshield) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [LICENSE.txt](LICENSE.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown and plain text reports with shell command and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local static-analysis reports with risk scores and optional quarantine guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
