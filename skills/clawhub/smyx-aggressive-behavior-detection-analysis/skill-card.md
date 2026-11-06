## Description:

Detects aggressive interactions in livestock and poultry from continuous barn videos, including fighting, biting, chasing and butting, and outputs behavior type, intensity level and alert level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock and poultry farm operators use this skill to review barn images and videos for aggressive interactions, assess their intensity and alert levels, and retrieve earlier analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected footage is sent to LifeEmergence, and account credentials persist locally.

Mitigation: Review before installing; use footage approved for this service, and ask the publisher to restrict credential destinations and separate secrets from account identifiers.

Risk: The export-only setting may not prevent uploads, and the API URL override may not select another server; server-side retention and account isolation are unverified.

Mitigation: Do not rely on those settings to prevent uploads or change the server. Ask the publisher to fix the export-only behavior and honor endpoint overrides; confirm retention and account isolation with the service operator.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis)
- [Skill introduction](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis results in JSON and Markdown tables for historical report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior segments, involved-animal locations, intensity and alert levels, and report links.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
