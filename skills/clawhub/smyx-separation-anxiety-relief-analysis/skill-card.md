## Description:

Analyzes videos of pets left alone for separation-anxiety behaviors and provides reports and comfort recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and boarding staff use the skill to review pet-alone footage, identify possible anxiety behaviors, and receive suggested comfort strategies or access past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-camera footage or video URLs may be sent to a third-party cloud service.

Mitigation: Use only footage approved for cloud processing and review its privacy implications before submitting it.

Risk: The skill may silently create or reuse an account identity and store tokens locally.

Mitigation: Review account and local credential-storage behavior before installation, and restrict access to the workspace.

Risk: History requests may retrieve cloud reports associated with the reused account identity.

Mitigation: Confirm the account context before requesting or sharing history reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-separation-anxiety-relief-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Markdown report or JSON analysis result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and a history table; results can be saved to a file.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
