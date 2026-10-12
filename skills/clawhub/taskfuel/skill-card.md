## Description:

Helps an agent discover and call paid APIs through the user's taskfuel.ai account and prepaid balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taskfuel.ai](https://clawhub.ai/user/taskfuel.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use this skill to find and call paid search, market data, enrichment, and other APIs through their taskfuel.ai prepaid account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation runs a remote CLI installer.

Mitigation: Review the installer before running it.

Risk: A connected account can transmit request data to third-party APIs.

Mitigation: Review the requested endpoint and obtain approval before sending sensitive payloads.

Risk: Small paid calls can occur without per-call confirmation and deplete prepaid balance.

Mitigation: Require approval for the first paid call, quote and cap each call, and monitor cumulative spending.

## Reference(s):

- [taskfuel skill listing](https://clawhub.ai/taskfuel.ai/skills/taskfuel)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and API responses (text or JSON)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid API calls are charged against the user's prepaid balance.]

## Skill Version(s):

0.5.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
