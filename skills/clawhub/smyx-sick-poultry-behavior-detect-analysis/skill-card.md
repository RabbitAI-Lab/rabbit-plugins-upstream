## Description:

Detects morbid behavioral cues in poultry and pigs from continuous barn videos — such as difficulty standing, ruffled feathers/piloerection, isolation, drowsiness and appetite loss — and outputs behavior type with risk level up to 2-3 days ahead of visible clinical signs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and livestock health teams use the skill to screen poultry or pig barn images and videos for abnormal behaviors, review risk levels, and query prior reports. Results support early screening and do not provide disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared accounts may expose other users’ historical reports.

Mitigation: Avoid shared-user deployment until report access is reliably bound to each sender.

Risk: The advertised export-only mode may still upload videos.

Mitigation: Require a fix and verify that export-only mode does not transmit footage before using it.

Risk: API secrets may be reused or credentials may appear in logs.

Mitigation: Require fixes for secret reuse and credential logging, and confirm account-enrollment and token-storage controls before installation.

Risk: Selected footage is sent to the service provider’s cloud, while cloud retention and server-side access enforcement were not tested.

Mitigation: Confirm acceptable data handling and verify cloud retention and server-side access controls before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-sick-poultry-behavior-detect-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis results, JSON, Markdown, Report links]

**Output Format:** [Structured behavior findings and risk levels in JSON or text; historical report lists in Markdown with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior categories, animal locations, group-level proportions, risk levels, and cloud report links; screening information only, not diagnosis or treatment advice.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
