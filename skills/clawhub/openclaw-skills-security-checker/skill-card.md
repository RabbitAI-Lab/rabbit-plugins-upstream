## Description: <br>
Security scanner for ClawdHub skills - detects suspicious patterns, manages whitelists, and monitors Moltbook for security threats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[digitaladaption](https://clawhub.ai/user/digitaladaption) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and skill maintainers use this skill to scan ClawdHub skills for suspicious patterns, manage trusted-skill whitelists, monitor security discussions, and generate human-readable or structured scan reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional install hooks can mediate future skill installs and block or allow skills based on scan results. <br>
Mitigation: Enable install hooks only after reviewing the referenced scripts and keep a backup of any shell-profile changes. <br>
Risk: Optional scheduled scans can run periodically and write scan logs or reports on the user's system. <br>
Mitigation: Configure cron jobs intentionally, review the paths before enabling them, and monitor generated reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/digitaladaption/skills/openclaw-skills-security-checker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration guidance] <br>
**Output Format:** [Markdown and JSON reports, command examples, and configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe optional install hooks, cron schedules, whitelist updates, and report paths for user review.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
