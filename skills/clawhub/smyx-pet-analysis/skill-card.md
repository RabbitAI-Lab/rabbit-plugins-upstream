## Description:

Analyzes uploaded pet videos or video URLs and returns a structured health report with potential concerns and care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers can submit a cat, dog, or bird video for a preliminary health report with potential concerns and care suggestions. The report is for reference and does not replace diagnosis by a veterinarian.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may silently create or reuse cloud accounts, store credentials locally, and send pet videos or URLs to an external provider.

Mitigation: Before use, disclose account creation and data uploads, use separate identities for different users, protect stored credentials, and verify that the no-analysis option works. Avoid sensitive media and shared workspaces until these controls are addressed.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured health analysis report with potential findings, care suggestions, and report links; history results are returned as structured data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts supported pet video files or video URLs; reports are for health reference only.]

## Skill Version(s):

999.999.1012 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
