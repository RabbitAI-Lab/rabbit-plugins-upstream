## Description:

Analyzes images or video for possible stranger proximity near minors and provides safety alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, school staff, and developers use the skill to analyze footage or images for possible stranger proximity near children, review safety warnings, and retrieve past analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, footage, or media URLs involving minors are sent to an external cloud service.

Mitigation: Use only with authorization for cloud processing of child-safety footage; confirm the provider's retention, access, and deletion policies.

Risk: The skill can create or reuse an internal identity and store service tokens locally.

Mitigation: Review account and session handling before use; protect local tokens and limit access to the running environment.

Risk: Cloud history queries can expose sensitive past reports.

Mitigation: Limit report access to authorized users and verify the provider's report access controls and deletion process.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-stranger-approach-warning-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or structured JSON, with Markdown report links for history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection results, safety recommendations, report links, and historical report listings; results can be saved to a file.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; artifact frontmatter lists 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
