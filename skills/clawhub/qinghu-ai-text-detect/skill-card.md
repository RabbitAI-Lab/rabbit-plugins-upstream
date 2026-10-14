## Description:

Checks submitted text for signs of AI generation and reports overall confidence, estimated AI-written share, category proportions, and segment-level results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and other users can submit text to a paid detection service to review AI-generation indicators, including passage-level findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install or upgrade unpinned third-party tooling and change the local Node environment or PATH.

Mitigation: Review installation steps and preinstall a reviewed, pinned qhkit version instead of allowing automatic setup.

Risk: Submitted text may be sent to a paid external detection provider.

Mitigation: Avoid submitting sensitive text without authorization; review the provider's terms and approve the estimated charge before calling the service.

Risk: AI-detection scores and manual fallback judgments may be mistaken for definitive authorship evidence.

Mitigation: Treat results as indicators, review passages in context, and clearly distinguish manual judgment from service-generated scores.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ai-text-detect)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written assessment with confidence estimates and segment details; optional table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits spent on paid calls; when detection is unavailable, labels any qualitative assessment as a manual judgment rather than a tool result.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
