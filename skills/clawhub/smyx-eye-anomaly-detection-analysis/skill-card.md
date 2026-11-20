## Description:

Analyzes close-up pet eye images or video for signs of redness, abnormal tearing, and opacity, then returns screening alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding staff, and veterinary teams can submit clear pet-face images or videos for a visual screening of redness, tearing, and eye opacity, or retrieve previous reports. Results are screening prompts and do not replace a veterinarian’s diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is rated suspicious because scanners report undeclared account and credential handling; reported behaviors include local profile and token storage and possible media uploads.

Mitigation: Avoid installation unless you are comfortable with those behaviors. Use only images you are comfortable sending for analysis, and verify account, token, and media handling before use.

Risk: An option described as avoiding analysis may still trigger it, and scan coverage is partial because a local reference did not resolve.

Mitigation: Do not rely on that option to prevent analysis; resolve and review the missing reference before relying on the scan as complete.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-eye-anomaly-detection-analysis)
- [API interface notes](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [Structured JSON reports with textual or Markdown summaries and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual screening output only; not a veterinary diagnosis.]

## Skill Version(s):

1.0.14 (server-resolved release metadata; artifact frontmatter says 1.0.23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
