## Description:

Ensures agents obtain the current date before answering relative-time or current-event questions so responses can be based on up-to-date tool results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[space-cadet](https://clawhub.ai/user/space-cadet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to make agents verify the current date before constructing searches or answers for relative-time and current-event requests. It is most useful in environments where stale dates or training-data assumptions can cause wrong-year queries or unsupported factual claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent environment may not provide a session_status-style current-date source, causing time-sensitive requests to stop or return warnings.

Mitigation: Install the skill only where an equivalent current-date tool is available, or document the fallback warning behavior for users.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, text]

**Output Format:** [Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an available session_status-style current-date source for time-sensitive queries; otherwise the agent should warn that the result may be inaccurate.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
