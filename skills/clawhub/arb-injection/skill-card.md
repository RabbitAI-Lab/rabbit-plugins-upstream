## Description: <br>
BYOCB ArbInjectionSkill scans EVM smart contracts for arbitrary call injection vulnerabilities, supports real-time chain monitoring, and can scan specific addresses. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[cryptotooldev](https://clawhub.ai/user/cryptotooldev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Solidity and blockchain security researchers, auditors, and developers use this skill to monitor supported EVM chains or scan specific contracts for potential arbitrary call injection issues. It is intended for educational and authorized security research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for persistent background monitoring and external user alerts, which can create unwanted notifications or operational exposure if enabled without clear approval. <br>
Mitigation: Run monitoring only with explicit user consent, isolate the environment, and confirm allowed alert channels before sending third-party notifications. <br>
Risk: The release evidence flags unpinned daily self-updates as a concern. <br>
Mitigation: Pin a reviewed commit or release, disable automatic daily updates unless required, and review changes before reinstalling dependencies. <br>
Risk: The skill may use API keys for optional LLM analysis. <br>
Mitigation: Limit API key scope, store credentials outside shared logs or outputs, and run scans with the optional LLM path disabled when it is not needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cryptotooldev/skills/arb-injection) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON] <br>
**Output Format:** [Markdown guidance with shell commands, configuration snippets, alert text, and references to JSON and Markdown scan results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve background monitoring, local result files, optional LLM-assisted analysis, and user alerts for high-severity findings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
