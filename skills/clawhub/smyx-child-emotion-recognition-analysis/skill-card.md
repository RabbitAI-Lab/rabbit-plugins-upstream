## Description:

Analyzes child monitoring media or media URLs with cloud APIs to classify visible emotions such as crying, anger, low mood, fear, or calm and return a structured report with soothing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as parents, teachers, or child-care operators use this skill to submit child monitoring media or a media URL for emotion classification, negative-emotion alerts, soothing hints, and history lookup. The output is intended as child-care communication support, not as a clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's videos, audio, or media URLs may be processed by remote cloud APIs.

Mitigation: Use the skill only with appropriate guardian or institutional consent and avoid submitting media when remote processing is unacceptable.

Risk: Report history may be linked to a persistent local or remote identity, and tokens may be stored in the workspace data database.

Mitigation: Install only if the publisher and backend service are trusted, and review local workspace data handling before using report history features.

Risk: Emotion classifications and soothing hints could be mistaken for clinical assessment.

Mitigation: Treat results as child-care communication support; do not use them as psychological diagnosis or clinical advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [Child emotion recognition API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with embedded JSON-style structured analysis, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud-hosted report history and may save report text to a user-specified output file.]

## Skill Version(s):

1.0.24 (source: server release evidence; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
