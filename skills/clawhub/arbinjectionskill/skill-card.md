## Description: <br>
BYOCB ArbInjectionSkill scans EVM smart contracts for arbitrary call injection vulnerabilities, monitors chains in real time, or scans specific addresses. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[cryptotooldev](https://clawhub.ai/user/cryptotooldev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Solidity and blockchain security researchers use this skill to monitor supported EVM chains or scan contract addresses for arbitrary CALL and DELEGATECALL injection patterns during authorized security review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to install and run external code as a persistent background monitor. <br>
Mitigation: Review dependencies before installation and pin the external repository to a specific audited commit before running it. <br>
Risk: The artifact recommends automatic daily git pull and npm install updates. <br>
Mitigation: Avoid unattended automatic updates; review and test updates before deploying them. <br>
Risk: Alerts may be sent to external messaging channels. <br>
Mitigation: Require explicit approval for each alert channel and verify high-severity findings before notifying users. <br>
Risk: Optional LLM analysis can use an API key and may send scan context outside the local environment. <br>
Mitigation: Use scoped API keys only when external analysis is acceptable for the contracts being reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cryptotooldev/skills/arbinjectionskill) <br>
- [Publisher profile](https://clawhub.ai/user/cryptotooldev) <br>
- [Project repository referenced by the skill artifact](https://github.com/BringYourOwnBot/arb-injection) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated JSON or Markdown finding reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are written to a results directory, and high-severity findings are intended for review before approved user alerting.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
