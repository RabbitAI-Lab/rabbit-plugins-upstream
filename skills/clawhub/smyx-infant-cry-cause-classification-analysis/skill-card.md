## Description:

Analyzes infant cry audio or audio-bearing video through a cloud-backed workflow to classify likely crying causes, return confidence information, provide soothing guidance, and link to generated reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators of baby-monitoring workflows use this skill to submit infant cry audio or audio-bearing video for likely-cause classification, confidence reporting, calming suggestions, and historical report lookup. Results are intended as parenting-support reference information, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant or household audio and video may be processed by a configured cloud backend.

Mitigation: Use only with guardian consent, review backend configuration and data handling terms, and confirm retention and deletion controls before using real child-monitoring recordings.

Risk: The workflow may silently create or reuse a local identity and persist token-bearing user records.

Mitigation: Review local identity and token storage before installation, run in a controlled environment, and clear or rotate stored tokens when access should end.

Risk: The scanner describes the implementation as a generic media analysis flow under an infant-cry label.

Mitigation: Validate the configured backend, expected scene code, and sample outputs before relying on results in a product workflow.

Risk: Cry-cause classifications and soothing suggestions may be incorrect or over-interpreted.

Mitigation: Present outputs as non-diagnostic parenting support and route persistent, abnormal, or symptom-accompanied crying to qualified medical care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-infant-cry-cause-classification-analysis)
- [Infant cry cause classification API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON-like analysis, status messages, calming guidance, and report links; optional saved text output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export URLs and historical report lists when requested.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
