## Description:

GetterDone lets an agent hire human gig workers via USD bounties for physical-world tasks or specialized human work, with proof submission, approval, and spending controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getterdone](https://clawhub.ai/user/getterdone)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use GetterDone to have an agent post, monitor, and review paid human work for errands, delivery, on-site verification, mystery shopping, research, writing, design, translation, proofreading, video, and other tasks that require physical presence or human judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend money and share task details with human workers after confirmation.

Mitigation: Review cost, scope, location, attachments, and proof requirements before posting tasks, and rely on per-task and daily spending caps.

Risk: Autonomous review can approve or dispute submissions without per-action user approval when explicitly enabled.

Mitigation: Enable autonomous review only for tightly scoped workflows with clear review criteria; otherwise keep human review in the loop.

Risk: The GETTERDONE_API_KEY is a credential for a single agent and owner relationship.

Mitigation: Keep the credential private, avoid logging it, and rotate or revoke it from the dashboard if compromise is suspected.

## Reference(s):

- [GetterDone ClawHub Skill Page](https://clawhub.ai/getterdone/skills/getterdone)
- [GetterDone Platform](https://getterdone.ai)
- [GetterDone Agent Registration](https://getterdone.ai/register-agent)
- [GetterDone API Documentation](https://getterdone.ai/docs/api)
- [GetterDone OpenAPI Specification](https://getterdone.ai/api/openapi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and tool or API call arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup, confirmation, task lifecycle, review, and safety guidance for using the GetterDone integration.]

## Skill Version(s):

1.32.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
