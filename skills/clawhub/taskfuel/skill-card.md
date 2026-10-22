## Description:

Let an agent discover and call paid APIs (search, market data, enrichment, and more) through the user's taskfuel.ai account, paid per call from their prepaid balance. Use when the user asks the agent to buy/call a paid API, mentions taskfuel.ai, or a task needs a paid capability (web search, tweet search, market data) the agent lacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taskfuel.ai](https://clawhub.ai/user/taskfuel.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Taskfuel to find suitable paid API endpoints and call them through the user's prepaid account for tasks such as web search, market data, and enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API calls can spend the user's prepaid balance without first getting approval for paid use.

Mitigation: Get explicit authorization before paid use, set a total task or session budget that includes charged polling, quote each endpoint before its first paid call, and cap calls at the approved amount.

Risk: The installation command downloads and runs a remote installer.

Mitigation: Review the installer before running it.

Risk: API requests may share user-provided data with endpoint providers, and the skill may submit endpoint ratings or problem reports.

Mitigation: Approve what data may reach providers and review feedback content to ensure it contains no secrets.

## Reference(s):

- [taskfuel.ai](https://taskfuel.ai/)
- [Taskfuel on ClawHub](https://clawhub.ai/taskfuel.ai/skills/taskfuel)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Text, Guidance]

**Output Format:** [CLI instructions and provider-dependent API responses, including text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful API calls may incur charges; response content depends on the selected endpoint.]

## Skill Version(s):

0.5.3 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
