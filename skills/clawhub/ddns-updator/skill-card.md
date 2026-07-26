## Description: <br>
Dynamic DNS updater for self-hosted, homelab, and edge devices that detects public IPv4 and IPv6 addresses, compares them with prior state, and updates configured DDNS records through dynv6. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kintansky](https://clawhub.ai/user/kintansky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, homelab operators, and edge-device administrators use this skill to check current public IP addresses and update DDNS records when addresses change. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update DDNS records using a provider token. <br>
Mitigation: Use a token scoped to the needed dynv6 zone and store it outside the skill directory in a chmod-600 config file. <br>
Risk: A broad public-IP request may trigger a DNS update attempt. <br>
Mitigation: Use explicit commands for DNS updates and separate IP-only checks from update requests. <br>
Risk: Optional cron scheduling can make updates automatic. <br>
Mitigation: Add cron only when automatic DDNS updates are intended, and review the schedule and script path before enabling it. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/kintansky/ddns-updator) <br>
- [ClawHub skill listing](https://clawhub.ai/kintansky/skills/ddns-updator) <br>
- [dynv6 update endpoint](https://dynv6.com/api/update?...) <br>
- [ipify IPv4 endpoint](https://api.ipify.org) <br>
- [ipify IPv6 endpoint](https://api64.ipify.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to run DDNS update scripts, read public IP data, and manage local configuration/state files.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata; artifact frontmatter declares 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
