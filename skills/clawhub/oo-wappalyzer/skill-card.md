## Description: <br>
Operates Wappalyzer through an OOMOL-connected account to discover subdomains, look up website technologies, verify email deliverability, and check account credits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to route Wappalyzer tasks through the OOMOL oo CLI, including technology lookup, subdomain discovery, email verification, and account credit checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs connector commands against a connected Wappalyzer account and can consume account credits. <br>
Mitigation: Inspect the live action schema before building each payload and review the exact command before execution. <br>
Risk: The skill depends on account connection and credential handling through OOMOL. <br>
Mitigation: Use the OOMOL connection flow for credentials and only run setup steps after an authentication or connection error. <br>
Risk: The security evidence advises trusting the publisher and limiting configured service access. <br>
Mitigation: Install only after confirming the OOMOL publisher handle and configure only Wappalyzer access the agent should be allowed to use. <br>


## Reference(s): <br>
- [ClawHub Wappalyzer skill page](https://clawhub.ai/oomol/skills/oo-wappalyzer) <br>
- [Wappalyzer homepage](https://www.wappalyzer.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [OOMOL Wappalyzer connection](https://console.oomol.com/app-connections?provider=wappalyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
