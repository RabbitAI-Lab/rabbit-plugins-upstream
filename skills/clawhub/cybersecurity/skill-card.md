## Description: <br>
Provides defensive cybersecurity guidance for alert triage, compromise investigation, attack-path analysis, vulnerability prioritization, detection, compliance evidence, and risk reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security practitioners, engineers, and operational leaders use this skill to scope suspected compromises, prioritize remediation, harden identity, endpoints, networks, cloud tenants and supply chains, write detections, and prepare defensible findings or audit evidence. It advises by default and requires written authorization before proposing live-system action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Durable local notes may contain sensitive security context such as incident summaries, findings, assets, vendors, contacts, and due dates. <br>
Mitigation: Protect the declared Clawic data folders and follow the skill guidance to keep credentials, raw evidence, and personal records out of those notes. <br>
Risk: Security guidance can become disruptive or legally sensitive when it touches live systems. <br>
Mitigation: Use the written authorization gate before live-system action; without scope, keep work to analysis, read-only review, tabletop exercises, detection logic, or remediation design. <br>
Risk: Reports and recommendations can be incomplete if local configuration, memory, logs, or evidence are missing. <br>
Mitigation: Keep observed, inferred, and recommended statements separate, label confidence, and verify important conclusions against authoritative evidence before operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/cybersecurity) <br>
- [Clawic Cybersecurity skill page](https://clawic.com/skills/cybersecurity) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Working file templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with structured findings, tables, checklists, detection logic, reports, and local note updates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write scoped local notes under declared Clawic data folders; evidence and secrets are represented by pointers, not stored.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
