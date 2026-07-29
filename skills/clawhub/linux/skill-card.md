## Description: <br>
Debugs and hardens Linux hosts across common administration failures, including permissions, storage, memory pressure, systemd, scheduling, networking, SSH, boot, packages, security baselines, desktop issues, and distribution differences. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and system administrators use this skill to triage Linux host failures, plan safer administrative changes, harden exposed machines, and maintain local operational notes and runbooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide destructive or lockout-prone Linux administration tasks, including storage, account, firewall, and remote-access changes. <br>
Mitigation: Review proposed commands before execution, keep rollback paths for remote changes, and validate configuration before applying changes. <br>
Risk: The security guidance flags ownership-changing guidance as needing correction in a future update. <br>
Mitigation: Review ownership-changing guidance manually and prefer least-scope ownership changes until the skill is updated. <br>


## Reference(s): <br>
- [ClawHub Linux skill page](https://clawhub.ai/ivangdavila/skills/linux) <br>
- [Clawic Linux skill page](https://clawic.com/skills/linux) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local note updates, rollback commands, validation checks, and operational runbooks when a session produces durable Linux administration outcomes.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
