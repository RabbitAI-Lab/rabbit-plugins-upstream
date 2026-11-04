## Description:

Summarizes overnight global events and maps them to potential opportunities and risks in China's A-share market before the opening bell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can request a pre-market briefing that summarizes overnight events, explains possible effects on A-share sectors, ranks areas to watch, and surfaces relevant risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance asks users to share an API key in chat, which can expose credentials.

Mitigation: Use protected local provisioning, restrict the configuration directory to mode 0700 and the credential file to mode 0600, and rotate any key already shared in chat.

Risk: The submitted package contains instructions but not the external runner, so its runtime behavior is uncertain.

Mitigation: Inspect and pin the external runner before executing it.

Risk: Queries consume Cue credits, and optional schedules continue until removed.

Mitigation: Check credit use before running and remove schedules when they are no longer needed.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Markdown report with event summaries, A-share sector implications, ranked opportunities, risk notes, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Based on public information; does not provide real-time market data, capital flows, or buy/sell points.]

## Skill Version(s):

1.0.9 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
