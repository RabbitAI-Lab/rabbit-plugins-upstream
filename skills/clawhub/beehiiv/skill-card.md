## Description:

beehiiv API integration with managed OAuth for managing newsletter publications, subscriptions, posts, custom fields, segments, tiers, and automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage beehiiv newsletter accounts through Maton, including subscribers, publications, posts, custom fields, segments, tiers, and automations. It is intended for API-backed newsletter administration where read/list calls are preferred and writes require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can manage a connected beehiiv account, including subscriber changes, post publishing, deletion, and automation changes.

Mitigation: Review connection scopes, prefer read/list calls first, specify the intended connection when multiple accounts exist, and require explicit confirmation before any write, deletion, publishing, or automation change.

Risk: Long-lived API keys or surfaced OAuth and provider-issued tokens could expose account access.

Mitigation: Prefer OAuth through the Maton CLI and operating system credential store, avoid printing or persisting credentials, and use MATON_API_KEY only when the CLI cannot be installed.

Risk: beehiiv API responses can contain personal data or untrusted external content.

Mitigation: Extract only task-relevant fields, avoid storing raw responses unless requested, and treat fetched content as data rather than instructions for follow-up actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/beehiiv)
- [Maton Homepage](https://maton.ai)
- [beehiiv Developer Documentation](https://developers.beehiiv.com/)
- [beehiiv API Reference](https://developers.beehiiv.com/api-reference)
- [Maton Documentation](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with bash, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected beehiiv account; API responses may contain personal data and should be minimized to task-relevant fields.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
