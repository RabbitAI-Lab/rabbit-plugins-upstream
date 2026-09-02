## Description:

Yuanjian yotta-triage is a zero-dependency, local static malware triage skill that hashes files, identifies file types, measures entropy, extracts classified strings and IOCs, parses PE and ELF headers, and reports risk hints without executing samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security analysts, incident responders, red-team and blue-team engineers, and agent users use this skill to perform authorized static first-look triage on suspicious files or sample directories. It produces hashes, file-type and entropy signals, PE/ELF details, classified strings, IOC lists, and risk hints for downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports can contain extracted URLs, domains, IP addresses, email addresses, file paths, and hashes from analyzed samples.

Mitigation: Run recursive scans only on directories the user is authorized to analyze and handle generated reports as potentially sensitive investigation artifacts.

Risk: Static risk levels are investigative hints and may be incomplete or misleading if treated as definitive malware verdicts.

Mitigation: Require analyst review and, when appropriate, corroborating dynamic analysis or threat intelligence before taking enforcement, attribution, or remediation decisions.

Risk: The installer can place the skill into multiple agent skill directories, which may make more agents load the skill than intended.

Mitigation: Install only into the specific agent directory needed for the workflow and avoid global or multi-agent installation unless that broader exposure is intentional.

## Reference(s):

- [Static triage specification](references/triage-spec.md)
- [Risk scoring model](references/risk-model.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-triage)
- [GitHub repository](https://github.com/YottaMeta/yotta-triage)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-triage)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Text, JSON, Markdown, or IOC-only JSON emitted by a local CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes communicate the highest risk hint: 0 for low-or-below, 1 for medium, 2 for high, 3 for critical, and 4 for usage or read errors.]

## Skill Version(s):

0.1.1 (source: frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
