## Description:

Using fixed cameras in kindergartens or early-education centers, the system analyzes multi-person video to detect social-interaction behaviors among children, including approach, conversation, cooperative play, and interaction heatmaps for teacher reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External educators, early-education staff, and authorized operators use this skill to submit kindergarten, early-education, or playground videos for child social-interaction analysis. It returns interaction counts, durations, initiator statistics, heatmaps, history-report links, and non-diagnostic attention prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends videos or URLs of children to a remote analysis service.

Mitigation: Use only with proper authorization plus guardian and school consent, and avoid submitting unnecessary or unauthorized recordings.

Risk: The skill can query cloud report history and may create local workspace data that stores service tokens or user profile data for reuse.

Mitigation: Review local storage and cloud-history access before deployment, restrict access to authorized operators, and rotate or remove stored credentials when no longer needed.

Risk: Social-interaction results may be misread as psychological or autism-spectrum diagnosis.

Mitigation: Present results as visual behavior statistics and educational attention prompts only; refer suspected developmental concerns to qualified medical professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-social-interaction-analysis-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include interaction statistics, initiator summaries, heatmap URLs, history-report tables, and saved output files when requested.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter and release changelog mention 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
