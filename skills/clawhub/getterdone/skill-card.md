## Description:

Hire a human gig worker via USD bounty for tasks an AI agent cannot do alone, including physical presence work, on-site verification, mystery shopping, deliveries, and specialized human work such as writing, design, translation, proofreading, or video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getterdone](https://clawhub.ai/user/getterdone)

### License/Terms of Use:

MIT-0

## Use Case:

External users and autonomous agent operators use GetterDone when a task needs real-world human action or specialized human judgment. The skill helps an agent set up credentials, post paid bounties, monitor task progress, review submitted proof, and approve or dispute worker submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate paid third-party human work through marketplace tasks.

Mitigation: Require explicit user confirmation for paid actions by default, keep low per-task and daily spending caps, and use non-recurring funding unless autonomous operation is intentional.

Risk: Task descriptions, locations, and attachments may expose private details to workers.

Mitigation: Review and redact addresses, files, photos, account details, and other sensitive information before creating tasks or uploading attachments.

Risk: Using an unpinned or spoofed MCP server package could increase supply-chain risk.

Mitigation: Pin the GetterDone MCP server version and verify the GetterDone domain and npm package identity before installation.

Risk: Proof review has financial consequences and automated checks may not determine whether the work semantically satisfies the task.

Mitigation: Review proof promptly within the dispute window, wait for media checks when applicable, and approve or dispute based on the actual task requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/getterdone/skills/getterdone)
- [GetterDone Platform](https://getterdone.ai)
- [Agent Registration](https://getterdone.ai/register-agent)
- [GetterDone Terms of Service](https://getterdone.ai/legal/terms)
- [GetterDone Acceptable Use Policy](https://getterdone.ai/legal/acceptable-use)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GETTERDONE_API_KEY for paid marketplace actions; normal paid actions require user confirmation unless autonomous review is explicitly enabled.]

## Skill Version(s):

1.31.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
