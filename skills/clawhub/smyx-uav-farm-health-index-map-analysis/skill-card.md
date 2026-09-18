## Description:

This skill analyzes UAV multispectral or high-resolution RGB farm imagery to generate vegetation-index health maps and identify crop-stress zones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural operators, drone service providers, cooperatives, and farm-analysis teams use this skill to turn UAV orthophotos, mosaics, or video into vegetation-index maps, abnormal-zone coordinates, area estimates, coverage statistics, and report links. Results are intended as field-management reference material and should be checked against on-site observations before operational decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload UAV imagery and submit image URLs to external analysis services.

Mitigation: Use only imagery that the user is authorized to share, remove unnecessary sensitive metadata where practical, and run first with non-sensitive test inputs.

Risk: The skill can create or reuse an internal identity and store account tokens locally.

Mitigation: Install in a controlled environment, document where identity and token state is stored, and use scoped test credentials until the publisher provides clear storage and rotation guidance.

Risk: The security evidence reports plaintext private development API endpoints by default.

Mitigation: Replace development HTTP endpoints with verified HTTPS production endpoints before operational use and review network destinations during deployment.

Risk: Automatic history access may expose prior analysis records associated with the resolved account.

Mitigation: Limit history-list use to accounts intended for this workflow and review account scoping before enabling shared or production deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-uav-farm-health-index-map-analysis)
- [UAV farm health index API reference](artifact/references/api_doc.md)
- [SMYX analysis API reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown report text with structured JSON content, report links, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local imagery or submit image URLs to external analysis APIs; supports history-list output when requested.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
