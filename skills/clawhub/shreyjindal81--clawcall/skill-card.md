## Description:

Helps an agent place and manage US phone calls, navigate menus and hold queues, connect users to live calls, and configure inbound answering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shreyjindal81](https://clawhub.ai/user/shreyjindal81)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent to call US businesses can handle scheduling, order follow-ups, phone menus, voicemail, and live handoffs. Users can also configure calling preferences and inbound answering.

### Deployment Geography for Use:

United States (US phone calls only)

## Known Risks and Mitigations:

Risk: Live calls and paid features can incur charges, and calls may be recorded or transcribed.

Mitigation: Confirm the user's calling limits and review service costs and recording behavior before calling.

Risk: Credentials and saved callback numbers are sensitive account data.

Mitigation: Keep credentials in the approved local store or secret store, restrict them to the ClawCall API, and retain callback numbers only for the user's workflows.

Risk: Call tasks may require payment cards, health information, government identifiers, or authentication secrets.

Mitigation: Do not collect or relay restricted data; arrange a live user handoff when necessary, or stop that part of the task.

Risk: The current calling guides are fetched remotely and may change or become unavailable.

Mitigation: Use only the designated HTTPS guide origin and stop new calls or configuration changes if the guides cannot be fetched or reconciled.

## Reference(s):

- [ClawCall calling guides](https://api.clawcall.dev/guides/v1/index.md)
- [ClawCall skill listing](https://clawhub.ai/shreyjindal81/skills/clawcall)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Conversational text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can initiate real phone calls and report their outcomes.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
