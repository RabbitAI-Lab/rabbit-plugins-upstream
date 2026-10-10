## Description:

Provides local, static triage of suspicious files and directories using hashes, file signatures, entropy, strings, and PE/ELF headers, producing reports and indicators of compromise without executing samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts and incident responders use this skill to inspect authorized suspicious files or directories offline, prioritize static indicators, and share IOC lists for further investigation. Its risk ratings are leads, not a malware verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer scripts write files into agent skill directories.

Mitigation: Review the install destination, run --dry-run first, and pin the npm version in sensitive environments.

Risk: Static signals and risk ratings can be mistaken for a confirmed malware diagnosis.

Mitigation: Treat findings as leads and corroborate them through authorized human review or other evidence.

Risk: Sample files or extracted indicators may contain sensitive information.

Mitigation: Analyze only files and directories you are authorized to access and handle reports accordingly.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-triage)
- [Publisher-listed project homepage](https://github.com/YottaMeta/yotta-triage)
- [Static triage specification](references/triage-spec.md)
- [Risk model](references/risk-model.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text, JSON, or Markdown triage report; optional JSON IOC list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-file hashes, static indicators, and risk leads; output to stdout or a local file.]

## Skill Version(s):

0.1.4 (source: frontmatter, CHANGELOG, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
