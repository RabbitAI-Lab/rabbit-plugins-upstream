## Description:

Turn approved messaging into an askable digital-human sales-readiness course.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales enablement and go-to-market teams use this skill to turn approved positioning, messaging, launch, and reference materials into an interactive digital-human readiness course with grounded voice Q&A and optional checks for understanding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or upgrade the PersonWise CLI before creating a course.

Mitigation: Require explicit approval and review the install or update command before it is run.

Risk: The workflow uses browser OAuth and a PersonWise account to create or publish courses.

Mitigation: Authenticate only through the PersonWise browser flow, avoid handling secrets, and confirm the intended account and access target.

Risk: Selected source materials may be uploaded to PersonWise and existing course credits may be consumed.

Mitigation: Use only user-selected materials, keep default course access private, and require new approval for additional courses, payments, broader visibility, or agent-discovered file uploads.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/personwiseai/skills/personwise-sales-enablement-training)
- [PersonWise publisher profile](https://clawhub.ai/user/personwiseai)
- [Signed PersonWise service descriptor](artifact/assets/service-descriptor.signed.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON payloads and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing workflow instructions for creating, reviewing, refining, publishing, or querying PersonWise courses; course artifacts are produced through the PersonWise CLI and service.]

## Skill Version(s):

2.1.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
