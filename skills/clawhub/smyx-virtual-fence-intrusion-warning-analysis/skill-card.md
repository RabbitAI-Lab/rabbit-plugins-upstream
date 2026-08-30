## Description:

Customizes safety zones, identifies babies crawling out or approaching dangerous areas such as bedsides/windowsills, and immediately alerts to protect baby safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze home monitoring video or image inputs for virtual fence crossings, unsafe boundary approaches, and related infant safety alerts. It can also retrieve cloud-stored historical warning reports for the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded home video, image content, or media URLs are sent to a remote analysis service.

Mitigation: Use only media that the user is authorized to process remotely, avoid unnecessary sensitive footage, and confirm the remote-processing expectation before installation or use.

Risk: The skill creates or reuses backend identity state and persists tokens locally.

Mitigation: Run it in an environment where local token persistence is acceptable, protect the working directory, and clear stored identity state when rotating users or decommissioning the skill.

Risk: The skill can retrieve cloud-stored historical reports with limited user control.

Mitigation: Limit use to the intended user context and review report access expectations before enabling history queries.

Risk: Virtual fence alerts are auxiliary safety signals and may be incomplete or incorrect.

Mitigation: Treat results as supplemental warnings and maintain physical safeguards and human supervision for infant safety.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-virtual-fence-intrusion-warning-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Virtual fence analysis API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown status text with structured JSON analysis content and optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis output may include report export links; history queries return cloud report records formatted from JSON.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
