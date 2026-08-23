## Description:

Analyzes pet camera images or videos for separation-anxiety behaviors, returns structured observations, severity levels, comfort recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet owners, and pet boarding operators use this skill to analyze pet-alone camera media for likely separation-anxiety behavior and to receive observation-oriented intervention suggestions. The skill is not a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-camera media may be uploaded or referenced by a remote service.

Mitigation: Use only media you are authorized to share, avoid sensitive household footage where possible, and confirm service retention and deletion controls before use.

Risk: The skill may create or reuse local identity state and retain authentication tokens for report history.

Mitigation: Run it in an isolated workspace, limit access to local state files, and remove stored identity or token state when the workflow is complete.

Risk: Behavior analysis and intervention suggestions may be mistaken for medical diagnosis.

Mitigation: Treat results as observation support only and consult a veterinarian or qualified behavior specialist for severe, persistent, or self-harming behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-separation-anxiety-relief-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet separation anxiety API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured analysis with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query historical reports and may write an output file when requested.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
