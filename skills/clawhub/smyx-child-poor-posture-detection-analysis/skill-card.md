## Description:

Analyzes child study-area video from a desk lamp or mounted camera to estimate posture metrics, detect hunchback or head tilt, generate reminder text, and return structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and product teams use this skill to analyze child posture videos for smart desk lamps, home study desks, or classroom monitoring workflows. It returns posture metrics, poor-posture classifications, reminder text, session summaries, and report links for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child video and report data is sent to cloud APIs.

Mitigation: Use only with guardian consent and clear controls for where video is processed, who can access report links, how long reports are retained, and how deletion is handled.

Risk: The skill silently creates or reuses persistent user identities and tokens.

Mitigation: Review identity/account binding and token storage before deployment, isolate access by user or installation, and remove or rotate credentials when access changes.

Risk: Visual posture estimates may be mistaken for medical assessment.

Mitigation: Present Cobb angle and head-tilt results as habit-correction guidance only, and direct users to qualified medical professionals for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [Analysis API error documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown text with structured JSON report content, reminder text, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a local file when an output path is provided.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter shows 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
