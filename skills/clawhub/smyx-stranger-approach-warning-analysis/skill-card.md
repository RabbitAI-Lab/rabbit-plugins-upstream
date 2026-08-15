## Description:

Detects the appearance of strangers near minors and actively issues safety reminder alerts to protect minor safety, suitable for homes, schools, childcare centers, and other scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and developers use this skill to analyze uploaded or URL-based monitoring images and videos for possible strangers near minors, then review structured alert reports and historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded images, videos, and provided URLs may be sent to the lifeemergence cloud service.

Mitigation: Use only with clear consent and with publisher assurances for retention, deletion, access control, and handling of media involving minors.

Risk: Reports may be tied to an automatically resolved or created identity, and local user or token data may be stored in the workspace.

Mitigation: Run in a controlled workspace, restrict access to generated reports and token storage, and confirm account deletion and report retention controls before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-stranger-approach-warning-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown or JSON analysis reports, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recognition results, risk prompts, recommendations, report links, and historical report tables.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata; artifact SKILL.md frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
