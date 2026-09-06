## Description:

Poly-Mal-Scan helps agents use FWold to scan PHP, JavaScript, and Bash source code for webshells, reverse shells, command injection, file-write backdoors, obfuscated payloads, and related malicious-code patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tsherryyann](https://clawhub.ai/user/tsherryyann)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and agent operators use this skill to run or integrate PHP, JavaScript, and Bash malware scanners through CLI or MCP workflows, triage suspicious code findings, and maintain detector rules. It supports source-file and content scanning, language routing, rule updates, regression checks, and troubleshooting scanner behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanner findings are security triage output and may be incomplete or require human judgment.

Mitigation: Review reported snippets, source locations, and threat categories before taking remediation action.

Risk: Rule JSON changes alter future scanner behavior and can affect detection quality.

Mitigation: Review rule updates and run the documented regression checks before accepting changed detector rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tsherryyann/skills/poly-mal-scan)
- [MITRE ATT&CK Enterprise Techniques](https://attack.mitre.org/techniques/enterprise/)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [GTFOBins](https://gtfobins.github.io/)
- [tennc webshell samples](https://github.com/tennc/webshell)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and inline shell or Python commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanner integrations return structured JSON findings with suspicious code snippets, threat categories, and source locations when available.]

## Skill Version(s):

0.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
