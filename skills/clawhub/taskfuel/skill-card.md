## Description:

Let an agent discover and call paid APIs, including search, market data, and enrichment, through the user's taskfuel.ai account with per-call billing from a prepaid balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taskfuel.ai](https://clawhub.ai/user/taskfuel.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use taskfuel to discover, quote, and call paid API endpoints through a connected taskfuel.ai account while enforcing approval and spend controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can trigger paid API calls against the user's taskfuel.ai prepaid balance.

Mitigation: Quote the first call to any endpoint, require explicit approval for calls over $0.10 or repeated calls, and set --max-amount to the approved quote before paying.

Risk: The skill may install the CLI with a remote shell script.

Mitigation: Review before installing and prefer a verified installer or package source instead of running the remote install script directly.

Risk: Endpoint behavior, quality, and pricing depend on upstream providers.

Mitigation: Inspect endpoint docs with taskfuel discover, use dry runs before payment, avoid blind retries after paid failures, and report concrete endpoint issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taskfuel.ai/skills/taskfuel)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce paid API responses, quoted prices, paid amounts, balance status, endpoint ratings, and feedback reports through the taskfuel CLI.]

## Skill Version(s):

0.3.0 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
