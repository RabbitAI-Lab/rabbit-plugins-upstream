## Description: <br>
Automated Hunter-Killer pipeline for BlackArch reconnaissance, CVE-MCP enrichment, human-verified exploit triage, and bug bounty report preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1beekeeper](https://clawhub.ai/user/1beekeeper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External security researchers and internal security teams use this skill to plan authorized bug bounty or internal vulnerability discovery workflows, including reconnaissance, scanning, CVE enrichment, triage, and report drafting. It is intended for in-scope targets with explicit permission and human review before exploitation or disclosure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can actively probe third-party systems and has weak built-in scope and rate controls. <br>
Mitigation: Run it only against explicit in-scope targets with documented authorization, target allowlists, manual scope checks, and low scan rates. <br>
Risk: Automated scanning and exploit triage can produce false positives or encourage unsafe follow-up testing. <br>
Mitigation: Require human validation before exploitation, report submission, or disclosure, and avoid destructive tests or data exfiltration. <br>
Risk: Scanner output and discovered secrets may include sensitive third-party data. <br>
Mitigation: Store findings in controlled locations, redact secrets in reports, and follow the relevant bug bounty platform's data-handling rules. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/1beekeeper/skills/bug-bounty-pipeline) <br>
- [ARGUS homepage](https://github.com/nousresearch/argus) <br>
- [Wayback CDX API](https://web.archive.org/cdx/search/cdx?url=*.$domain/*&output=text&fl=original&collapse=urlkey) <br>
- [FIRST EPSS API](https://api.first.org/data/v1/epss?cve={cve_list}) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash, Python, and report-template code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces reconnaissance, scanning, enrichment, triage, and reporting workflow snippets for an agent to adapt under human supervision.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
