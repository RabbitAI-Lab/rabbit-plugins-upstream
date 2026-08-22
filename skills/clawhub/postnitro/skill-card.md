## Description:

PostNitro helps an agent create on-brand social media carousels, single-image posts, and short videos, then draft or schedule them across LinkedIn, Instagram, TikTok, and Threads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iammuneeb](https://clawhub.ai/user/iammuneeb)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to automate PostNitro workflows for generating or importing social content, rendering designs or videos, and scheduling drafts or live posts through connected social accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected PostNitro workspace can schedule or publish real social posts.

Mitigation: Confirm the account, platform, content, and scheduled time before any SCHEDULED action, and use DRAFT when unsure.

Risk: The PostNitro API key grants access to the user's PostNitro automation workflow.

Mitigation: Prefer POSTNITRO_API_KEY or --api-key on shared machines, avoid persistent credentials when possible, and restrict any saved config file permissions.

Risk: Some documented CLI commands delete schedules, disconnect social accounts, or delete audio records.

Mitigation: Require an explicit user confirmation for destructive commands and verify target IDs before using commands that require --yes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iammuneeb/skills/postnitro)
- [PostNitro Homepage](https://postnitro.ai)
- [PostNitro CLI Reference](references/cli-reference.md)
- [PostNitro CLI Examples](examples/EXAMPLES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill's documented CLI workflow returns JSON from PostNitro commands and may produce design, PDF, PNG, or MP4 URLs through the service.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
