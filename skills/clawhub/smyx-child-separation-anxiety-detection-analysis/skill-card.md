## Description:

Using a fixed camera at the home entrance or kindergarten gate, the system analyzes pre-school videos and detects crying facial expressions (frowning, open-mouth crying, tearing), physical clinging actions (grabbing parent's clothes, hugging parent's leg, pulling door frame), and resistance behaviors (stepping back, lying on the ground), then comprehensively evaluates the separation-anxiety level (mild / moderate / severe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, teachers, and childcare teams can use the skill to review drop-off videos for crying, clinging, and resistance behaviors, then receive a structured observation report and soothing suggestions. It is intended to support early awareness and does not provide a psychological diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports undisclosed account and credential handling, possible transfer of sensitive video, and unclear export-only behavior.

Mitigation: Before installation, request clear details about account and credential handling, remote services and data sent, and confirmation of export-only behavior; avoid uploading child video until these points are clarified.

Risk: The security assessment is incomplete because it reports a missing local reference and cannot establish the behavior of unavailable components.

Mitigation: Review the missing reference and assess unavailable components before use.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report in JSON, with text summaries and Markdown tables for report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include observed behaviors, an estimated separation-anxiety level, and supportive suggestions; this is not a psychological diagnosis.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter declares 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
