## Description:

元鉴 yotta-triage helps agents perform offline, read-only static triage of suspicious files or sample directories by computing hashes, identifying file types, measuring entropy, extracting categorized strings and IOCs, parsing PE/ELF headers, and reporting risk hints rather than malware verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security analysts, incident responders, malware analysts, and developers use this skill to quickly inspect authorized suspicious files or sample folders without executing them. It produces static triage reports and IOC lists for follow-up human review, sandboxing, or threat-intelligence workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can persistently copy the skill into agent skill directories.

Mitigation: Install to a specific trusted agent or directory, and prefer pinned package versions or reviewed package contents for repeatable installs.

Risk: Reports may contain hashes and extracted IOCs from analyzed files.

Mitigation: Analyze only files and directories the user is authorized to inspect, and handle generated reports according to the sensitivity of the source samples.

Risk: Static risk scoring may be mistaken for a definitive malware verdict.

Mitigation: Treat risk levels as triage hints and confirm conclusions through human review, sandboxing, or threat-intelligence correlation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-triage)
- [YottaMeta yotta-triage repository](https://github.com/YottaMeta/yotta-triage)
- [triage-spec.md](references/triage-spec.md)
- [risk-model.md](references/risk-model.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, plus generated triage reports in text, JSON, Markdown, or IOC-only JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk levels are static hints only; reports may include file hashes and extracted IOCs.]

## Skill Version(s):

0.1.3 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
