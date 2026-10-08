## Description:

Coordinates research, drafting, evidence checks, methodology review, and peer review for academic papers and other substantive long-form writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

Writers, researchers, and analysts use this skill to produce evidence-backed long-form articles, academic papers, and industry analyses with staged human approval and quality review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow creates multiple project files and may expose sensitive material in working drafts.

Mitigation: Review the Phase 0 consent gates, keep project inputs within an approved workspace, and avoid including unredacted confidential material.

Risk: Research requests can send search terms or URLs to external services.

Mitigation: Approve only the external-service categories needed for the task and sanitize search topics before consenting.

Risk: Declared tool restrictions may not be enforced by the host configuration.

Mitigation: Check the OpenClaw host tool permissions before use and restrict execution-capable tools independently of the skill's declarations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quick start](QUICKSTART.md)
- [Workflow and deliverables](references/deliverables.md)
- [Permissions and consent](references/permissions.md)
- [External research services](references/_shared/真源/external-services.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown documents and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes research notes, drafts, audit and peer-review reports, and advisory publication suggestions.]

## Skill Version(s):

2.16.1 (source: ClawHub release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
