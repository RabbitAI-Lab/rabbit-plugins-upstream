## Description: <br>
Security gatekeeper for skill installations that performs deep code analysis to detect malicious patterns, credential access, data exfiltration, command injection, and other security risks before installing skills from ClawHub, GitHub, or external sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amir-ag](https://clawhub.ai/user/amir-ag) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill as a pre-install security scanner for external agent skills. It reviews skill files for known malicious patterns and produces risk-scored findings that can guide manual review or automated installation gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to activate around installation-related prompts and may run when a user discusses adding or installing skills. <br>
Mitigation: Treat scanner output as advisory and confirm that scan results apply to the intended skill before using them to approve or block installation. <br>
Risk: The scanner reads local skill artifacts in order to analyze them. <br>
Mitigation: Run it only against skill directories you intend to review, and avoid granting broader filesystem access than needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/amir-ag/skills/clawhub-skill-scanner) <br>
- [Threat Patterns Reference](references/threat-patterns.md) <br>
- [ClawHavoc campaign article](https://www.esecurityplanet.com/threats/hundreds-of-malicious-skills-found-in-openclaws-clawhub/) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [ClawHub](https://clawhub.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain-text security report or JSON scan result, with shell exit codes for installation gating] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes risk score, risk level, recommendation, scanned file counts, line counts, and per-finding details when JSON output is requested.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
