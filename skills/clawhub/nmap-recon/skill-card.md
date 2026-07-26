## Description: <br>
Nmap Recon helps agents propose authorized Nmap reconnaissance and port-scanning commands, parse common Nmap outputs, and choose scan profiles for service and vulnerability discovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nsahal](https://clawhub.ai/user/nsahal) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Security developers, penetration testers, and authorized operations teams use this skill to plan Nmap scans, identify open ports and exposed services, run selected Nmap script categories, and summarize scan output. It is intended only for systems the user owns or has explicit permission to assess. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Network scanning can affect systems outside the user's authority or scope. <br>
Mitigation: Confirm the target, scope, and explicit permission before using generated Nmap commands; avoid public or third-party systems without written approval. <br>
Risk: Aggressive, vulnerability, UDP, or stealth scans may disrupt monitored or production environments. <br>
Mitigation: Use approved scan profiles, timing, and maintenance windows for sensitive systems, and review each command before execution. <br>


## Reference(s): <br>
- [Nmap Recon on ClawHub](https://clawhub.ai/nsahal/skills/nmap-recon) <br>
- [Publisher profile: nsahal](https://clawhub.ai/user/nsahal) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with bash command examples and concise explanatory guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local Nmap installation and an authorized target scope before commands are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
