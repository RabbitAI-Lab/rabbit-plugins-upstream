## Description:

Plan, budget, quote, generate, and recover AI video through the authenticated MaxVideoAI remote MCP connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[camgraphe](https://clawhub.ai/user/camgraphe)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan AI video projects, compare models, estimate budgets, request exact quotes, approve paid generation, and recover generated results from their authenticated MaxVideoAI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid generation could be confirmed before the user approves the exact current quote.

Mitigation: Prepare a fresh quote for the exact request and call confirmation only after explicit approval of that quote.

Risk: An ambiguous timeout could lead to a duplicate paid request.

Mitigation: Recover the accepted job with status or recent-generation lookup and do not create a replacement paid request after an ambiguous timeout.

Risk: Credentials, payment details, private media, or signed locations could be exposed in chat or durable skill files.

Mitigation: Use the MaxVideoAI OAuth and account flows, keep payment handling on MaxVideoAI, and avoid copying private bytes or signed locations into durable files.

## Reference(s):

- [Safe generation boundary](references/safe-generation.md)

## Skill Output:

**Output Type(s):** [text, guidance, API calls, configuration]

**Output Format:** [Markdown or plain text with structured tool-driven results and MaxVideoAI result destinations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account-aware model comparisons, budget estimates, exact quotes, generation status, and result or library destinations; credentials and payment details are not collected in chat.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
