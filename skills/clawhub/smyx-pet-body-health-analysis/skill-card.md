## Description:

Identifies obesity, emaciation, external injuries, skin abnormalities, and abnormal mental states, helping pet owners detect health issues promptly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners and care teams use this skill to analyze pet images, videos, local files, or media URLs for body condition, skin abnormalities, visible injuries, activity state, and related health guidance. Agents can also use it to return structured reports, report links, and history summaries when the user requests prior pet body condition reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet photos, videos, or private media URLs may be sent to lifeemergence.com services for analysis.

Mitigation: Review the skill before installation, confirm user consent for cloud analysis, and submit only media intended for this service.

Risk: The skill may create or reuse a local account identity and store returned tokens in the workspace data directory.

Mitigation: Make account and persistence behavior opt-in where possible, restrict workspace access, and clear stored tokens when they are no longer needed.

Risk: Automatic cloud history lookup may query prior pet body condition reports associated with the local account identity.

Mitigation: Use history lookup only when the user asks for prior reports and explain that results come from the cloud service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-body-health-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON analysis reports with report links and optional Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call cloud services to analyze pet media or retrieve history; media input is limited to documented image and video formats up to 10 MB.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
