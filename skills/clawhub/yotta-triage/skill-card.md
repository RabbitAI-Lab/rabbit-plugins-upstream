## Description:

元鉴 yotta-triage is a local, offline static malware triage skill that hashes files, identifies file types, measures entropy, extracts classified strings and IOCs, parses PE and ELF headers, and reports risk hints without executing samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security analysts, incident responders, malware-analysis learners, and agent operators use this skill to perform an authorized first-pass static triage of suspicious files or sample directories. It produces local reports and IOC lists that support follow-on human review, sandboxing, or threat-intelligence workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled installers can copy agent-executable skill files into multiple assistant skill directories without confirmation.

Mitigation: Install only into the intended assistant skill directory, preferably with an explicit --dir path or specific --agent target; avoid global or no-argument installer modes unless broad installation is intended.

Risk: Unpinned npx installation can retrieve whatever package version is current at install time.

Mitigation: Pin the npm package version when reproducibility or change control matters.

Risk: The skill analyzes suspicious or malicious samples and its findings are static risk hints rather than malware verdicts.

Mitigation: Use it only on files and directories the operator is authorized to analyze, and confirm conclusions with human review, sandboxing, or threat intelligence before taking action.

## Reference(s):

- [Triage specification](references/triage-spec.md)
- [Risk model](references/risk-model.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-triage)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Text, JSON, Markdown, or IOC-only JSON reports emitted to stdout or an output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include file hashes, detected type, entropy, extracted string categories, PE or ELF metadata, risk level, risk reasons, and IOC records.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
