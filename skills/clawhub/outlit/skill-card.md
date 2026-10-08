## Description:

Guides agents in using Outlit customer intelligence to investigate accounts, analyze customer data, and manage authorized workspace changes through available tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leo-paz](https://clawhub.ai/user/leo-paz)

### License/Terms of Use:

MIT-0

## Use Case:

Customer-success teams and developers use this skill to investigate onboarding, adoption, retention, renewal, and expansion using Outlit customer records and analytics. With explicit authorization, they can also configure workspace capabilities and review customer identity changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Piping a downloaded installer into a shell can execute unreviewed code.

Mitigation: Prefer the documented npm or Homebrew installation paths when practical.

Risk: Workspace write grants can change access, destinations, integrations, activation, settings, Features, or identity records.

Mitigation: Confirm the intended change and grant only the permissions needed before allowing write actions.

Risk: Customer merges are irreversible and can combine unrelated records.

Mitigation: Review the merge preview and execute only after clear authorization and confirmation that both records identify the same customer.

## Reference(s):

- [Outlit documentation](https://docs.outlit.ai/)
- [Outlit documentation index](https://docs.outlit.ai/llms.txt)
- [Outlit homepage](https://outlit.ai)
- [Outlit ClawHub release](https://clawhub.ai/leo-paz/skills/outlit)
- [Customer identity and merge workflow](references/identity.md)
- [SQL reference](references/sql-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, SQL, Configuration guidance]

**Output Format:** [Markdown with inline commands and query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should distinguish evidence from interpretation; workspace changes require explicit authorization.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
