## Description:

Set up an autonomous, customer-facing support agent inside an Intercom inbox across WhatsApp, Instagram, Facebook, in-app Messenger, SMS, and email; the agent reads customer screenshots, transcribes voice notes, and hands conversations to humans cleanly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othreecodes](https://clawhub.ai/user/othreecodes)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams and developers use this skill to configure an OpenClaw agent that answers customers directly through Intercom-connected channels and escalates to humans when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill configures an agent to respond to real customers with Intercom permissions and a teammate identity.

Mitigation: Get support-workspace owner authorization, use a dedicated Intercom app with only required permissions, and pilot on one low-risk channel before widening rollout.

Risk: An overbroad support agent may answer unrelated questions or be influenced by customer-provided instructions.

Mitigation: Scope the agent explicitly to the product and monitor early conversations before expanding channel coverage.

Risk: Customer screenshots may be misidentified if the agent guesses which app or product they show.

Mitigation: Instruct the agent to describe visible details, trust the customer's stated context, and ask clarifying questions instead of naming apps from screenshots.

Risk: A broad or hard-to-rotate Intercom token could increase impact if the integration is misconfigured.

Mitigation: Use a dedicated bot app, grant least-privilege access, and keep the token easy to revoke or rotate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othreecodes/skills/intercom-support-channel)
- [openclaw-intercom README and config reference](https://github.com/othreecodes/openclaw-intercom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes rollout guidance for permission scoping, token handling, channel limits, and human hand-off.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
