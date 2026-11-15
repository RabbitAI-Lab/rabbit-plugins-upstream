## Description:

Through fixed enclosure cameras, the system periodically captures tail images of geckos and lizards and uses AI visual analysis to detect tail length, tail-tip wounds, scabs, or abnormal shortening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers use the skill to review gecko and lizard tail images, track changes against historical measurements, and receive structured tail-loss alerts and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner flags account and credential handling, remote media uploads, and export-only behavior as insufficiently explained for the skill’s stated purpose.

Mitigation: Clarify and review these behaviors before installation; follow the scanner guidance to avoid installing until they are understood.

Risk: The security scan was partial because a referenced local path was missing, so it did not cover every referenced behavior.

Mitigation: Review the missing referenced material and the uncovered behavior before relying on the skill.

## Reference(s):

- [API interface and input guidance](references/api_doc.md)
- [Skill introduction demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Structured analysis reports in JSON or concise text, with Markdown tables for history queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report image-based tail measurements, event classifications, alert levels, and keeper guidance.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
