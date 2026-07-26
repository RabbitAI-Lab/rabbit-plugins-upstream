## Description: <br>
Data247 lets agents perform Data247 lookup and account actions through an OOMOL-connected oo CLI workflow without handling raw API tokens. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run Data247 phone intelligence, Do-Not-Call, account balance, and first-name gender inference actions through their connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Phone numbers and names used with this skill may be sensitive data sent through the OOMOL oo connector for Data247 lookups. <br>
Mitigation: Confirm the user intends to use OOMOL as an intermediary, treat lookup inputs as sensitive, and run actions only through the connected account. <br>
Risk: First-time setup can involve installing the oo CLI or opening account connection and billing flows. <br>
Mitigation: Review the oo CLI installer and OOMOL connection flow before first use, and run setup steps only after a matching command failure. <br>
Risk: Using an outdated or assumed action payload can produce incorrect requests. <br>
Mitigation: Inspect the live connector schema for the selected Data247 action before constructing the JSON payload. <br>


## Reference(s): <br>
- [ClawHub Data247 Skill](https://clawhub.ai/oomol/skills/oo-data247) <br>
- [Data247 Homepage](https://www.data247.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, json] <br>
**Output Format:** [Markdown guidance with bash commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId when run with --json.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence release and frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
