## Description:

Helps agents manage files, folders, sharing, and collaborations in an authorized Box account through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to find, upload, download, organize, and share Box content, and to manage collaborations in accounts they have authorized. Requested automations can connect Box actions to Maton functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Box authorization could expose sensitive files or permit unwanted changes.

Mitigation: Confirm the intended Box account, scopes, and connection ID; use least privilege and remove unused connections.

Risk: Uploads, shares, collaboration changes, and deletions can disclose or alter content.

Mitigation: Review the target, recipients, payload, and intended effect, and obtain explicit approval before each change.

Risk: Webhooks, functions, triggers, or destinations can create ongoing access or event forwarding.

Mitigation: Approve each automation and destination separately, verify its endpoint and scope, and remove it when no longer needed.

## Reference(s):

- [ClawHub Box skill](https://clawhub.ai/byungkyu/skills/box)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Box API reference](https://developer.box.com/reference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Box API calls may return structured data or file content from the authorized account.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
