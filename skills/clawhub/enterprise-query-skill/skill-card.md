## Description: <br>
Enterprise Query helps Chinese-speaking users run paid business registration lookups by company name or unified social credit code and returns structured registration details after Yeeap payment verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hehang195-sys](https://clawhub.ai/user/hehang195-sys) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to purchase and retrieve Chinese business registration information for supported company keywords. The agent creates an order, routes payment through yeeap-wallet, and returns the lookup result only after payment credentials are available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install an external payment skill globally for all agents. <br>
Mitigation: Review and approve the yeeap-wallet dependency before installation, especially in shared or managed agent environments. <br>
Risk: The submitted package contains instructions but not the scripts it tells the agent to execute. <br>
Mitigation: Install only where the expected scripts are supplied and reviewed, and stop execution if required scripts are missing. <br>
Risk: The workflow handles paid orders and payment credentials. <br>
Mitigation: Follow the artifact's credential-handling constraints: do not expose payCredential values, do not read raw order files with general file tools, and avoid logging sensitive payment data. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/hehang195-sys/yeeap-enterprise-query-skill) <br>
- [ClawHub skill listing](https://clawhub.ai/hehang195-sys/skills/enterprise-query-skill) <br>
- [yeeap-wallet dependency](https://github.com/Yeepay-Open-Platform/yeeap-wallet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese Markdown or plain text with shell and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid lookup flow; payment credentials must not be shown to the user or written to business logs.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
