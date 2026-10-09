## Description:

Analyzes outdoor surveillance images and videos for people, vehicles, non-motorized vehicles, and pets, and provides monitoring reports and report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Homeowners, farm operators, and outdoor-site managers use this skill to review surveillance images or videos for people, vehicles, and pets, and to retrieve monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outdoor surveillance images, videos, or URLs are sent to configured LifeEmergence cloud services.

Mitigation: Only submit footage or URLs you are authorized to share with the service.

Risk: The skill persists cloud identity and token state, and report histories may be mixed across users in shared workspaces.

Mitigation: Use a separate workspace per user and avoid shared-workspace report queries until identity isolation is fixed.

Risk: Detection results may be incomplete or inaccurate for security decisions.

Mitigation: Treat reports as advisory and verify suspected intrusions through appropriate security procedures.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-outdoor-monitoring-analysis)
- [Outdoor monitoring API documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured JSON or Markdown report with results, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, or JSON detail and optional file output; can list historical reports.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
