## Description:

Finds, downloads, exports, and verifies open-access Chinese medical literature using Weipu OA and Yiigle sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to retrieve open-access Chinese medical articles, export citation metadata, and verify Chinese references for literature reviews, guideline work, and citation checking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package security verdict is suspicious because the bundled tracker can send reports through a hardcoded private SSH host to Feishu.

Mitigation: Review and scan the package before deployment, and do not use the tracker notification path unless the destination and credentials are intentionally approved.

Risk: The --notify tracker behavior copies reports to a hardcoded host and uses remote Feishu credentials.

Mitigation: Remove or disable that path, or require a user-configured destination with host-key verification before enabling notifications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/cn-med-oa)
- [Weipu OA API contract](references/weipu-oa-api-contract.md)
- [Weipu OA platform](https://oa.cqvip.com)
- [Yiigle full-text database](https://rs.yiigle.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands plus JSON, RIS, PDF, HTML, and report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write downloaded PDFs, cn_refs.json manifests, cn_refs.ris exports, report.html/report.json verification reports, tracker reports, and local cache files.]

## Skill Version(s):

2.3.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
