## Description:

Analyzes child surveillance images or videos to identify negative emotions, produce structured reports, issue soothing reminders, and notify caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, schools, daycare operators, and developers use this skill to analyze child monitoring images or videos for negative emotion signals and retrieve structured reports or historical report lists. The results are advisory and should not replace adult supervision or emergency response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's surveillance media may be sent to external cloud services.

Mitigation: Use only with appropriate guardian or user awareness and consent, and avoid uploading unnecessary or sensitive footage.

Risk: Analysis reports may be retained and queried later.

Mitigation: Confirm retention expectations before use and limit access to report links and historical report queries.

Risk: The skill may create or reuse an account-linked identity and store service tokens.

Mitigation: Review identity handling and token storage before installation, especially in shared or regulated environments.

Risk: Emotion recognition results may be incomplete or misleading.

Mitigation: Treat reports as decision support only and rely on direct adult review for care, safety, or emergency decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call cloud APIs with image or video files or URLs, poll for results, and list retained reports linked to an internal identity.]

## Skill Version(s):

1.0.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
