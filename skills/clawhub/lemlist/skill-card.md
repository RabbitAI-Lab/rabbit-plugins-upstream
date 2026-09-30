## Description:

Helps agents manage Lemlist campaigns, leads, activities, schedules, and unsubscribes through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and their agents use this skill to review and manage Lemlist outreach campaigns and leads, and to set up approved automation through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the wrong Lemlist account or exposing a long-lived API key can grant unintended access.

Mitigation: Confirm the account and connection before authorization, prefer OAuth, and avoid displaying or persisting API keys.

Risk: Campaign, lead, and automation changes may affect recipients or modify account data.

Mitigation: Review the target and intended effect, then explicitly approve each write or automation action before execution.

Risk: Trigger destinations may keep forwarding event data after the initial setup.

Mitigation: Approve each destination separately, confirm its URL and data scope, and remove it when no longer needed.

## Reference(s):

- [ClawHub Lemlist skill](https://clawhub.ai/byungkyu/skills/lemlist)
- [Maton](https://maton.ai)
- [Lemlist API reference](https://developer.lemlist.com/api-reference)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions use the authorized Lemlist connection; changes require user approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
