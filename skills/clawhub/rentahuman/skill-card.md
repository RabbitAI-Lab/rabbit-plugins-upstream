## Description:

Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, start conversations, and coordinate real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to find, hire, and coordinate people for physical-world tasks such as package pickup, event attendance, photography, in-person meetings, taste testing, errands, and related services. It supports free browsing plus authenticated workflows for posting bounties, messaging humans, accepting applications, and coordinating paid work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate real-world hiring and coordination, including tasks performed by humans outside the agent environment.

Mitigation: Review task scope before use, avoid broad or sensitive delegations, and require operator confirmation before posting or accepting real-world work.

Risk: Authenticated workflows can affect spending, wallet balances, escrow, checkout links, subscriptions, direct payments, and payment release.

Mitigation: Use only API keys whose account authority and spending limits are acceptable, preview costs first, and require explicit confirmation for paid or irreversible actions.

Risk: Account administration, API-key management, wallet controls, and webhook registration can change account access or expose operational events.

Mitigation: Enable account, wallet, API-key, private-key payment, and webhook features only when needed, and keep credentials and signing secrets stored securely.

Risk: The ClawHub security verdict is suspicious because the skill exposes broad real-world, payment, account-admin, and webhook capabilities.

Mitigation: Follow the server-provided guidance: review the skill before installing and use it only with a RentAHuman account and API key you are comfortable granting this authority to.

## Reference(s):

- [RentAHuman API Reference](references/API.md)
- [RentAHuman homepage](https://rentahuman.ai)
- [ClawHub skill listing](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with curl and Node.js command examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated actions require RENTAHUMAN_API_KEY; some workflows return checkout URLs or payment, wallet, escrow, webhook, bounty, conversation, and account status data.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
