## Description:

Analyzes images or videos of economic crop leaves to identify likely crop-specific diseases and produce structured findings for initial assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and agricultural users can review images or short videos of corn, potato, peanut, and tomato leaves for likely diseases, or retrieve prior analysis reports. Results support visual screening and do not provide treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Report access may be shared unintentionally if sender isolation is not fixed.

Mitigation: Avoid shared multi-user workspaces until sender isolation has been corrected and verified.

Risk: Analysis can upload images or videos to a service and may incur service charges; export-only mode may still trigger cloud analysis.

Mitigation: Confirm uploads and possible charges are acceptable, avoid sensitive media, and do not rely on export-only mode to prevent uploads.

Risk: The skill uses a cached account database.

Mitigation: Protect the cached account database from access by other users.

## Reference(s):

- [API interface notes](artifact/references/api_doc.md)
- [Skill introduction demo](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured disease analysis in JSON and historical report lists in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include crop and disease identification, confidence, symptom descriptions, and report links; results are for initial screening.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata; bundled SKILL.md frontmatter reports 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
