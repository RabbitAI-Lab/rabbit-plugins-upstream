## Description:

Expands disease identification for economic crops such as corn, potato, peanut, and tomato by analyzing leaf images or videos and returning standardized visual disease-recognition results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit economic-crop leaf images, videos, or URLs for crop-specific visual disease screening and to retrieve prior analysis reports. The skill is for initial visual recognition and does not provide treatment or prevention advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party remote service receives crop images, videos, or URLs for analysis.

Mitigation: Avoid submitting sensitive media or private/internal URLs unless the publisher documents backend handling, retention, and account behavior.

Risk: The skill can silently create or reuse identity state and link cloud history to that identity.

Mitigation: Review the publisher's account and history behavior before deployment, and use isolated identities when testing.

Risk: Identity records and tokens may be stored in a local SQLite database.

Mitigation: Limit local filesystem access, protect the runtime environment, and remove local state after use when persistence is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Economic crop disease API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON report text, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include disease type, confidence, symptom description, analysis time, and report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact SKILL.md frontmatter is 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
