## Description:

Let an agent discover and call paid APIs (search, market data, enrichment, and more) through the user's taskfuel.ai account, paid per call from their prepaid balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taskfuel.ai](https://clawhub.ai/user/taskfuel.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover, quote, and call paid APIs through a connected taskfuel.ai account when a task needs a paid capability such as web search, tweet search, market data, or enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables paid API calls from a prepaid taskfuel.ai balance.

Mitigation: Require a quote before payment, get explicit user approval for larger or repeated spending, and pass the approved quote as a max amount.

Risk: The skill includes automatic CLI installation guidance.

Mitigation: Ask the user to confirm installation before running installer commands.

Risk: Connecting the account gives the agent access to paid API capabilities.

Mitigation: Have the user approve account connection in the browser and confirm intended use before spending funds.

## Reference(s):

- [taskfuel skill page](https://clawhub.ai/taskfuel.ai/skills/taskfuel)
- [taskfuel CLI installer](https://taskfuel.ai/install.sh)
- [taskfuel app dashboard](https://app.taskfuel.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide paid API discovery, quoting, and calls through the taskfuel CLI; responses can include command output and API response text.]

## Skill Version(s):

0.2.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
