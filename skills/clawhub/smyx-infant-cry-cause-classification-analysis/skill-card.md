## Description:

Classifies likely causes of infant crying from audio or audio-video input, returning confidence, secondary causes, acoustic feature summaries, and directional soothing guidance without providing medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, parents, childcare teams, and developers can use this skill to analyze authorized infant cry recordings or related history records for likely causes such as hunger, sleepiness, pain or discomfort, boredom, fear, colic, or unknown. The result is intended as a parenting support signal, not a clinical assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant recordings and history queries may be sent to a remote service for processing.

Mitigation: Process only recordings the user is authorized to submit, obtain guardian consent where applicable, and avoid submitting unnecessary sensitive background audio.

Risk: The skill silently creates or reuses an account identity and may persist authentication tokens in local workspace data.

Mitigation: Run the skill in an isolated workspace when possible, review local data storage before and after use, and clear stored API keys, tokens, or local database files when they are no longer needed.

Risk: Cry cause classification can be uncertain and is not a medical diagnosis.

Mitigation: Treat outputs as directional parenting support and seek professional care for persistent abnormal crying or symptoms such as fever, vomiting, or signs of distress.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-infant-cry-cause-classification-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Infant cry classification API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance, Files]

**Output Format:** [Markdown or JSON structured analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cry detection status, dominant cause, confidence, secondary cause probabilities, cry duration, acoustic feature summaries, soothing hints, history records, report links, and optional saved output files.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
