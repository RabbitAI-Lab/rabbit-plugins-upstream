## Description:

Scan documentation for broken links using curl. Use when validating markdown docs, checking for dead URLs, or before releasing documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[147258xuan](https://clawhub.ai/user/147258xuan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use the skill to find broken external links during reviews, before releases, and in CI/CD pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports that crafted links in scanned documentation can trigger shell commands.

Mitigation: Avoid scanning untrusted documentation or running with access to sensitive files or secrets; wait for a reviewed fix and clarified tool scope.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/147258xuan/skills/broken-link-checker)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text report or JavaScript results object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports checked links and any failures with file and line references; results depend on the target directory and network responses.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
