## Description: <br>
Hire humans for physical-world tasks via RentAHuman.ai. Search available humans by skill, post bounties, start conversations, and coordinate real-world work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to find human workers, post bounties, start conversations, and coordinate real-world tasks such as package pickup, event attendance, photography, errands, and taste testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can support high-impact real-world, account, messaging, payment, and webhook workflows. <br>
Mitigation: Require explicit user confirmation before public posts, payments, messaging, webhook registration, wallet changes, or other money-moving and account-level actions. <br>
Risk: Task descriptions and messages may expose sensitive physical-world information such as home addresses, access codes, tracking numbers, IDs, or schedules. <br>
Mitigation: Share only the minimum information required for the task and avoid sending sensitive personal or access details unless the user has reviewed and approved them. <br>
Risk: Using a broad RentAHuman API key may grant an agent account-level authority beyond simple browsing. <br>
Mitigation: Install and run the skill only with an API key the user is comfortable delegating, and keep read-only browsing separate from authenticated actions where possible. <br>


## Reference(s): <br>
- [RentAHuman homepage](https://rentahuman.ai) <br>
- [RentAHuman API reference](references/API.md) <br>
- [ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON payload examples, and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only browsing can use public endpoints; bounty, messaging, application, payment, webhook, and account-related actions require a RentAHuman API key and explicit user review.] <br>

## Skill Version(s): <br>
1.19.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
