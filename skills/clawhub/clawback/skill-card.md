## Description: <br>
Mirror congressional stock trades with automated broker execution and risk management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mainfraame](https://clawhub.ai/user/mainfraame) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use Clawback to configure an agent-accessible trading bot that monitors congressional disclosure sources and can execute scaled E*TRADE brokerage orders with risk controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can handle E*TRADE credentials and may be configured with real-money trading authority. <br>
Mitigation: Use the E*TRADE sandbox first, avoid production keys until the code has been reviewed, and grant only the brokerage permissions needed for the intended account. <br>
Risk: Local Clawback configuration and token files may contain sensitive brokerage or notification credentials. <br>
Mitigation: Restrict permissions on ~/.clawback and avoid sharing logs, debug output, or configuration files that may contain secrets. <br>
Risk: Debug authentication scripts and unattended cron or service setup can create high-impact side effects if used with live credentials. <br>
Mitigation: Do not run debug auth scripts with real credentials, and review any cron, systemd, sudo, or background trading setup before enabling unattended execution. <br>
Risk: Automated trading based on disclosure data can lose money or act on stale, incomplete, or incorrectly parsed information. <br>
Mitigation: Review trading parameters, position limits, and disclosure results before live use, and keep sandbox or manual confirmation steps in place until behavior is understood. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mainfraame/skills/clawback) <br>
- [E*TRADE Developer portal](https://developer.etrade.com) <br>
- [House Clerk disclosures](https://disclosures-clerk.house.gov) <br>
- [Senate eFD search](https://efdsearch.senate.gov) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local Clawback configuration and guide execution of CLI commands when invoked by an agent.] <br>

## Skill Version(s): <br>
1.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
