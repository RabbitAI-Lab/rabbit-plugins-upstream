## Description: <br>
Perform a security audit on exposed AI service endpoints using OpenClaw threat intelligence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to assess exposed AI service endpoints, summarize authentication and exposure risks, and produce hardening recommendations for services such as Open-WebUI, Ollama, and LocalAI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Endpoint audit workflows can prompt users for sensitive service details. <br>
Mitigation: Share only the minimum endpoint information needed for the audit and do not paste API keys, passwords, or service tokens. <br>
Risk: Firewall, package-upgrade, and service-install commands can affect production availability or access. <br>
Mitigation: Review commands before use, test changes where possible, and apply production changes during an approved maintenance window. <br>


## Reference(s): <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown security report with tables, checklists, and inline shell or configuration blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include endpoint risk ratings, hardening steps, verification checks, and ongoing monitoring guidance.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
