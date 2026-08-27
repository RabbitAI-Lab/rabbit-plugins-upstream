## Description:

OpenSpender lets agents discover and use paid web APIs, web search, model calls, and media generation through a user-funded allowance with prices, caps, receipts, and spending reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openspender](https://clawhub.ai/user/openspender)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use OpenSpender when a task needs paid API access without adding separate API keys or subscriptions. It guides the agent to inspect costs, respect caps, make paid calls, and report spend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid calls can spend from the user's OpenSpender allowance.

Mitigation: Set low per-request and daily caps, review the ledger, and require confirmation in the surrounding workflow when desired.

Risk: Allowance tokens grant bounded spending authority if exposed.

Mitigation: Store tokens only in an environment variable or secret store, and re-mint a card if a token is pasted into chat or source files.

Risk: Retrying denied or duplicate paid requests can create avoidable spend.

Mitigation: Do not split tasks to bypass caps, do not resubmit pending media jobs, and report cap denials or settled failures to the user.

## Reference(s):

- [OpenSpender skill page](https://clawhub.ai/openspender/skills/openspender)
- [OpenSpender homepage](https://openspender.com)
- [OpenSpender protocol reference](https://openspender.com/llms.txt)
- [OpenSpender canonical skill](https://openspender.com/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands, tool names, URLs, and cost-reporting text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide paid API calls and should report cost, cap denials, and receipts when money is spent.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
