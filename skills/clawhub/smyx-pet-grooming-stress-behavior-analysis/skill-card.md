## Description:

Analyzes pet grooming videos or video URLs through server-side APIs to identify stress behaviors such as struggling, panting, and tail tucking and return a stress-level report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, groomers, veterinary clinics, and pet-care teams use this skill to submit grooming-session media for stress behavior observation, stress-level grading, report links, and history lookup. The artifact describes the results as behavior observation support and says it does not provide disease diagnosis or behavior-correction plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Grooming media or URLs are sent to configured lifeemergence.com services for analysis.

Mitigation: Use only approved media, avoid sensitive footage unless retention and access controls are understood, and review the service relationship before installation.

Risk: The skill may create or reuse a cloud identity and store authentication tokens locally.

Mitigation: Run it in an isolated workspace or approved account context, restrict access to the workspace data directory, and clear stored tokens when the skill is no longer needed.

Risk: History lookup retrieves cloud-stored reports associated with the resolved identity.

Mitigation: Confirm the identity context before history queries and avoid shared workspaces where report access could cross users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis)
- [API 接口文档](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with JSON-formatted structured results and report links; optional saved text output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud history tables and exported report image links when the history-list workflow is used.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
