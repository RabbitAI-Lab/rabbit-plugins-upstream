## Description:

Grades the ripeness of crop fruit from images or videos using visible color, size, and gloss features, and suggests a harvest window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and agricultural teams use fruit images or videos to assess ripeness stages for crops such as tomatoes and peppers, plan harvest timing, and review past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or media URLs are sent to an external analysis service.

Mitigation: Use only media approved for external processing, and disclose the transfer before use.

Risk: The skill can silently create or reuse an identity and register or log in remotely.

Mitigation: Confirm that users accept automatic account linkage before enabling the skill.

Risk: Session tokens persist in a local workspace database, and cloud history is linked to the derived identity.

Mitigation: Restrict access to the workspace and historical reports; review retention and token removal procedures before deployment.

## Reference(s):

- [Fruit ripeness grading API documentation](artifact/references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crop-fruit-ripeness-grading-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown analysis reports and historical-report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ripeness grades, harvest-window guidance, and report links when available.]

## Skill Version(s):

1.0.13 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
