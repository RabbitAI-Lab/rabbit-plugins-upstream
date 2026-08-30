## Description:

taskfuel lets an agent discover and call paid APIs through the user's taskfuel.ai account, with each paid call charged against the user's prepaid balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taskfuel.ai](https://clawhub.ai/user/taskfuel.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to discover paid API capabilities, obtain price quotes, call allowed endpoints, and rate or report endpoint quality through a taskfuel.ai account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may spend small amounts from the user's prepaid taskfuel.ai balance without explicit per-call approval.

Mitigation: Require explicit user approval before every paid call, quote the exact request first, and repeat approved calls with a matching max amount.

Risk: Repeated or failed paid calls can compound spend or obscure whether the user was charged.

Mitigation: Avoid blind retries after paid errors, check the balance when charge status is unclear, and ask the user before continuing.

## Reference(s):

- [ClawHub taskfuel Skill Page](https://clawhub.ai/taskfuel.ai/skills/taskfuel)
- [taskfuel CLI Installer](https://taskfuel.ai/install.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include paid API call proposals, dry-run quotes, spending limits, and endpoint rating or reporting guidance.]

## Skill Version(s):

0.2.8 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
