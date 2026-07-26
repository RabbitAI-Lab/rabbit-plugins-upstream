## Description: <br>
Perform a security audit on exposed AI service endpoints using OpenClaw threat intelligence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[Leek-w](https://clawhub.ai/user/Leek-w) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators of self-hosted AI services use this skill to collect endpoint details, assess OpenClaw threat-intelligence indicators, and produce hardening guidance for exposed services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for endpoint details that may be sensitive in an agent conversation. <br>
Mitigation: Share only endpoint information you are comfortable disclosing and avoid pasting secrets, credentials, or private infrastructure notes. <br>
Risk: The skill makes strong threat-intelligence claims without evidence of a concrete lookup mechanism. <br>
Mitigation: Treat breach, leaked credential, threat actor, and CVE findings as advisory unless the agent provides exact source and query evidence. <br>
Risk: The skill may suggest privileged firewall, package-management, or host-hardening commands. <br>
Mitigation: Review placeholders, backup needs, and access impact before manually running commands on the intended host. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/Leek-w/ai-security-audit) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown report with tables, checklists, and inline bash/configuration code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes endpoint risk summary, threat-intelligence findings, remediation steps, and verification checks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
