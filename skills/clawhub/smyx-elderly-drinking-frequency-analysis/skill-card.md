## Description:

Analyzes fixed-camera video of an elder's cup area to count cup-pickup events and produce directional dehydration-risk reminders for families or caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, caregivers, nursing-home staff, and elder-care platform operators use this skill to analyze camera footage of a cup placement area, summarize drinking-frequency signals, and decide whether to remind an older adult to drink water. It provides behavior-based reminders rather than medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private in-home or care-facility video may be processed by external network services.

Mitigation: Use only with clear consent from the monitored person or legal representative, review configured service endpoints before deployment, and confirm retention and access controls for uploaded footage and generated reports.

Risk: The artifact silently handles identity and report-history access, which can reduce user control over account linkage and stored reports.

Mitigation: Validate identity, token storage, and report access behavior in the deployment environment before use, and restrict access to historical reports to authorized caregivers or operators.

Risk: Cup-pickup frequency is only an indirect proxy for hydration and may be wrong when the cup is empty, handled by someone else, or shared.

Mitigation: Treat outputs as directional care reminders, combine them with caregiver confirmation and personal baselines, and seek medical advice for persistent low intake or symptoms.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-drinking-frequency-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured analysis reports with optional saved text output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include drinking-frequency metrics, dehydration-risk labels, caregiver reminder text, report links, and Markdown tables for historical report queries.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter states 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
