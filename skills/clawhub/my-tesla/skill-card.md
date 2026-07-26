## Description: <br>
Control Tesla vehicles from macOS via the Tesla Owner API using teslapy for authentication, vehicle status, lock and unlock, climate, charging, location, mileage tracking, and other remote vehicle commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[officialpm](https://clawhub.ai/user/officialpm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to inspect Tesla vehicle state, generate chat-friendly reports, and run explicit remote vehicle commands through a local Python CLI. It is intended for users who are comfortable granting Tesla account access and managing local vehicle data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Tesla account access and can send remote vehicle commands. <br>
Mitigation: Install only when the user accepts that access, and review command intent before running actions that affect the vehicle. <br>
Risk: Tokens, raw vehicle JSON, precise location output, and mileage exports can contain private information. <br>
Mitigation: Keep generated files local, avoid sharing logs or exports, prefer sanitized JSON outputs, and protect ~/.my_tesla/mileage.sqlite on shared machines. <br>
Risk: Disruptive actions such as unlocking, charging changes, windows, trunk, sentry mode, honk, flash, and charge-port commands can affect the vehicle state. <br>
Mitigation: Use the documented confirmation gates and require explicit user approval before passing --yes to safety-gated commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/officialpm/skills/my-tesla) <br>
- [Publisher profile](https://clawhub.ai/user/officialpm) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Files] <br>
**Output Format:** [Plain text status messages, JSON objects, CSV or JSON mileage exports, and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local authentication, defaults, and mileage database files under the user's home directory.] <br>

## Skill Version(s): <br>
0.1.64 (source: server release evidence, VERSION.txt, and changelog, released 2026-01-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
