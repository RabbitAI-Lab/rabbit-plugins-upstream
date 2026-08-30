## Description:

Monitors employee on-duty status in defined workplace areas from images, videos, or media URLs, and reports absence, post-leaving, and related status events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Facility managers, security teams, and operations staff use this skill to analyze workplace camera images, videos, or media URLs for on-duty presence, post-leaving, and absence events. The skill can also retrieve identity-linked historical monitoring reports from the provider service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace camera images, videos, media URLs, report outputs, and identity-linked metadata may be sent to the provider's remote services.

Mitigation: Review the provider's retention, deletion, access-control, and employee-notice practices before use, and avoid private camera URLs or sensitive footage unless those requirements are acceptable.

Risk: The skill silently creates or reuses local account state for report association.

Mitigation: Run the skill in a scoped workspace, use approved identity controls, and periodically review or clear local account state according to organizational policy.

Risk: Monitoring results may influence workplace supervision decisions and can be incomplete or incorrect.

Mitigation: Treat reports as decision support, require human review, and apply the organization's workplace management and employee-notice policies before taking action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-staff-absence-detection-analysis)
- [Personnel absence monitoring API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Markdown or JSON text reports, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured monitoring results, status counts, absence duration, recommendations, report links, and historical report lists.]

## Skill Version(s):

1.0.14 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
