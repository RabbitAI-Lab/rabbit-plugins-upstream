## Description:

Analyzes pet video, with optional audio, to detect sneeze and cough events, classify patterns such as dry or wet coughs, count frequency, and return a structured observation report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as pet owners, veterinary staff, and pet boarding operators use this skill to submit pet activity videos or URLs for respiratory behavior observation, frequency tracking, and historical report lookup. The output is behavioral analysis for monitoring support, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, audio, media URLs, and identity-linked report data are sent to vendor cloud services for analysis and history lookup.

Mitigation: Use only media that is appropriate to upload to the vendor service, avoid sensitive home footage, and confirm vendor retention and account practices before deployment.

Risk: The skill can silently create or reuse an account-linked identity and store access tokens in a local workspace database.

Mitigation: Run the skill in an isolated workspace, restrict workspace access, and clear local token or database files when the analysis history is no longer needed.

Risk: The analysis is behavioral observation and may be wrong or incomplete for medical decisions.

Mitigation: Treat the output as monitoring support only and direct frequent, severe, or unclear symptoms to a veterinarian.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown text containing structured JSON-style analysis results, history lists, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the returned report text to a user-specified output file.]

## Skill Version(s):

1.0.9 (source: server release metadata and target metadata; artifact frontmatter states 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
