## Description:

AI-powered intelligent customer service for banking and securities that supports FAQ answering, account inquiry, transaction guidance, complaint handling, and 24/7 automated support for China financial institution customer service teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Financial institution customer service teams use this skill to draft compliant banking and securities support responses, route intents, handle complaints, and define escalation behavior for account, transaction, product, and service inquiries.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Financial customer-service responses may expose or mishandle sensitive account, transaction, identity, or complaint information.

Mitigation: Customize the skill to enforce the institution's identity-verification steps, retention rules, data-minimization practices, and official business rules before production use.

Risk: Generic complaint SLAs, trigger phrases, and escalation rules may conflict with an institution's approved procedures.

Mitigation: Review and replace example SLAs, routing triggers, escalation paths, and forbidden language with the institution's current approved policies.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/gechengling/skills/security-intelligent-cs)
- [ClawHub publisher profile](https://clawhub.ai/user/gechengling)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown and plain text guidance with optional structured tables and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed and adapted to the institution's official business rules, identity-verification requirements, retention policies, and complaint SLAs.]

## Skill Version(s):

3.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
