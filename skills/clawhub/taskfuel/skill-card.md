## Description:

Lets an agent discover and call paid APIs, such as search, market data, and enrichment, through the user's taskfuel.ai account with charges paid from a prepaid balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taskfuel.ai](https://clawhub.ai/user/taskfuel.ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to discover, quote, call, recover, and rate paid APIs through a connected taskfuel.ai account while managing per-call spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can spend a user's prepaid taskfuel.ai balance on paid API calls.

Mitigation: Quote the first call to each endpoint, require explicit approval for calls over $0.10 or repeated paid loops, and pass the approved quote as a per-call maximum.

Risk: The installation path can run a remote shell installer for the taskfuel CLI.

Mitigation: Review the installer before use and install only when the user accepts that setup path.

Risk: Requests may send task data to upstream paid API providers.

Mitigation: Avoid sending secrets or private data and confirm that the selected provider and endpoint are appropriate before paying.

Risk: A broad trigger for paid capabilities can lead to unexpected spending decisions.

Mitigation: Use endpoint discovery and full endpoint documentation before each new paid call, and stop for user confirmation before large or repeated spends.

## Reference(s):

- [ClawHub taskfuel skill page](https://clawhub.ai/taskfuel.ai/skills/taskfuel)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides paid API discovery, quotes, calls, result recovery, endpoint ratings, and feedback through the taskfuel CLI.]

## Skill Version(s):

0.4.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
