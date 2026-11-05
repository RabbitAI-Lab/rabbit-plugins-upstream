## Description:

Performs local, offline static triage of authorized files and directories, producing hash, file-type, entropy, string, PE/ELF, risk-hint, and IOC reports without executing samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts and developers use it to triage files they are authorized to examine, review static indicators, and pass candidate IOCs to downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer scripts write into agent skill directories and may replace an existing installation.

Mitigation: Choose one target, preview with --dry-run, and back up customized installations before installing.

Risk: Static risk levels and extracted IOCs are clues; they do not determine whether a sample is malicious, and IOC reputation is not checked online.

Mitigation: Have an authorized analyst corroborate findings with independent analysis or intelligence sources.

## Reference(s):

- [Static triage specification](references/triage-spec.md)
- [Risk scoring model](references/risk-model.md)
- [Project homepage](https://github.com/YottaMeta/yotta-triage)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-triage)
- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-triage)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Text, JSON, or Markdown triage reports; JSON IOC list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-file static findings and clue-level risk hints, with aggregated IOCs.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata, SKILL.md frontmatter, CHANGELOG 2026-11-01, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
