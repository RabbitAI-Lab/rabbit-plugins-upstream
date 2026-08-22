## Description:

taskfuel lets an agent discover and call paid APIs, such as search, market data, and enrichment, through the user's taskfuel.ai account with charges paid per call from the user's prepaid balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taskfuel.ai](https://clawhub.ai/user/taskfuel.ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs paid API capabilities, including web search, tweet search, market data, enrichment, or similar provider-backed calls, through a connected taskfuel.ai account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad authority to spend from the user's taskfuel.ai prepaid balance.

Mitigation: Require a dry-run quote before paid use, explicit user approval for paid calls, and a maximum amount on approved calls.

Risk: The skill can send request data to paid upstream API providers.

Mitigation: Review endpoint documentation and request payloads before execution, and avoid sending secrets or unnecessary sensitive data.

Risk: The installation path shown in the artifact uses a remote shell script.

Mitigation: Prefer a verified, user-run installation method before enabling the CLI for agent use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taskfuel.ai/skills/taskfuel)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls]

**Output Format:** [Markdown guidance with inline shell commands and plaintext command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses quote, maximum amount, approval, balance, and rating guidance around paid taskfuel CLI calls.]

## Skill Version(s):

0.2.7 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
