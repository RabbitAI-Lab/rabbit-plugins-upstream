## Description:

Ensures accurate current-date queries by requiring the agent to retrieve the exact current date before handling relative-time or current-event requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to make assistants anchor relative-time and current-events answers to the current session date before searching or responding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Relative-time or current-events answers may use stale dates if the agent skips the current-date check.

Mitigation: Require the agent to retrieve the current session date first, compute absolute date ranges from that result, and avoid filling gaps with training data.

Risk: Current-date or real-time data lookup can fail or return incomplete information.

Mitigation: Tell the user when current-date or real-time evidence is unavailable instead of presenting unsupported dates as fact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentforge-cyber/skills/time-awareness)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to obtain the current date before answering relative-time or current-events questions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
