## Description:

Analyzes pet monitoring videos for signs of anxiety, howling, or prolonged isolation and returns a structured report with suggested soothing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and pet care operators use the skill to review monitoring videos for signs of distress and receive behavior observations, suggested responses, and links to reports. It can also retrieve prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private video may be uploaded even when export-only processing is requested.

Mitigation: Avoid private footage until export-only behavior is fixed, and confirm who owns the selected account and how the service retains and deletes videos.

Risk: Account setup may silently register or reuse an account and save login tokens.

Mitigation: Verify account ownership and credential handling; do not use a reusable API secret as an account identity.

Risk: Advertised soothing actions may not work without verified device integration.

Mitigation: Treat results as analysis and suggestions until device integration is verified; supervise any intervention.

## Reference(s):

- [Pet analysis API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report; historical report listings can be presented as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include observations, suggested actions, and report links.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
