## Description: <br>
Control Little Snitch firewall on macOS. View logs, manage profiles and rule groups, monitor network traffic. Use when the user wants to check firewall activity, enable/disable profiles or blocklists, or troubleshoot network connections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to inspect Little Snitch status, review logs, manage profiles and rule groups, and troubleshoot macOS network connections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Privileged Little Snitch commands can change firewall profiles, rule groups, preferences, backups, restores, or traffic capture behavior. <br>
Mitigation: Prefer read-only status and log commands first, and approve sudo commands or configuration changes only when specifically requested. <br>
Risk: Enabling Little Snitch command line access can expose powerful firewall controls to processes with elevated privileges. <br>
Mitigation: Enable CLI access only on trusted macOS systems and take precautions that untrusted processes cannot gain root privileges. <br>


## Reference(s): <br>
- [Little Snitch command line documentation](https://help.obdev.at/littlesnitch5/adv-commandline) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may include read-only Little Snitch checks and sudo-gated firewall, profile, rule-group, preference, backup, restore, and traffic-capture operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
