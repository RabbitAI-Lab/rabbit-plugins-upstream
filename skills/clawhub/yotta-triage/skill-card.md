## Description:

Performs offline static triage of local files and folders, reporting hashes, file characteristics, risk clues, and indicators of compromise without executing samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts, developers, and incident responders use this skill to inspect authorized local samples and produce triage reports and IOC lists for follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can replace existing skill files at the selected destination.

Mitigation: Preview with --dry-run and confirm the intended agent or directory before installation.

Risk: Reports may contain sensitive strings or indicators extracted from analyzed files.

Mitigation: Write reports to a separate protected location and review them before sharing.

Risk: Static risk levels are preliminary clues and do not establish whether a sample is malicious.

Mitigation: Have an analyst verify findings with other intelligence sources before making a decision.

Risk: Remote package contents and runtime behavior were not verified for this release.

Mitigation: Prefer verified local files or a verified, pinned npm release.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-triage)
- [Static triage specification](references/triage-spec.md)
- [Risk model](references/risk-model.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Text, JSON, or Markdown triage reports; optional IOC-only JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local static-analysis results and risk clues; samples are not executed.]

## Skill Version(s):

0.1.5 (source: ClawHub release evidence, frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
