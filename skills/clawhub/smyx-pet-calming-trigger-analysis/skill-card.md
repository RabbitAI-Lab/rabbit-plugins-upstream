## Description:

Analyzes pet videos through a remote service and returns behavior reports, recommendations, and links to historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and care providers use this skill to analyze monitoring footage for signs of distress and retrieve prior analysis reports. It does not itself play audio or control pet devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media or video URLs are sent to remote services for analysis.

Mitigation: Review the destination services and obtain appropriate consent before submitting media or URLs.

Risk: The skill automatically looks up cloud reports and stores identity and token data locally.

Mitigation: Review access to cloud reports and protect locally stored identity and token data before installing.

Risk: The pet-soothing description may imply audio playback or device control that the skill does not provide.

Mitigation: Use the results as analysis only; do not rely on this skill to operate soothing devices.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-calming-trigger-analysis)
- [Pet analysis API documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured text or JSON with report links; historical reports may appear as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can print results or save them to a local file]

## Skill Version(s):

1.0.17 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
