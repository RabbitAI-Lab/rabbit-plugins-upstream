## Description:

Identifies weeds and estimates coverage density from field images or video, providing distribution data for precision weeding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm managers and agricultural advisers use field imagery to identify weeds, assess coverage and distribution, and review past analyses to inform precision weeding decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Field media or URLs are sent to a third-party cloud service.

Mitigation: Use only with field data approved for cloud processing and review the destination before submitting media.

Risk: A shared fallback identity and locally stored service tokens may expose cloud report history across users in the same workspace.

Mitigation: Avoid shared workspaces or use isolated per-user environments and restrict access to locally stored credentials and reports.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or a Markdown report-list table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include weed density, distribution data, report links, and an optional saved result file.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; bundled SKILL.md says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
