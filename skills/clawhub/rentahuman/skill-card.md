## Description:

Hire humans for physical-world tasks via RentAHuman.ai by searching available humans, posting bounties, starting conversations, and coordinating real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find and hire people for real-world errands, events, creative review, package pickup, photography, and similar physical-world tasks. The skill helps agents browse profiles, create funded bounties, message workers, and manage applications through RentAHuman.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate funded real-world hiring actions and account/payment operations through an API key.

Mitigation: Require the agent to preview the bounty cost, exact total, worker details, and task details, then obtain explicit user confirmation before posting, accepting, paying, changing API keys, creating webhooks, or using wallet features.

Risk: Physical-world task descriptions may expose sensitive personal or logistical information.

Mitigation: Avoid including home addresses, access codes, government IDs, payment details, or sensitive schedules unless strictly necessary, and minimize any sensitive details that must be shared.

Risk: The available account and payment capabilities are broader than the main skill description suggests.

Mitigation: Limit authenticated use to the specific user-requested workflow and do not use wallet, webhook, API-key management, or payment-related actions unless the user explicitly asks for them.

## Reference(s):

- [RentAHuman API Reference](references/API.md)
- [RentAHuman](https://rentahuman.ai)
- [ClawHub Skill Page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with shell commands, JavaScript CLI usage, and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses RENTAHUMAN_API_KEY for authenticated write operations; public browsing operations do not require authentication.]

## Skill Version(s):

3.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
