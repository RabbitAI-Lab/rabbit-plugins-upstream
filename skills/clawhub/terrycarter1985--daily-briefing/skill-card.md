## Description:

Generate a concise daily briefing by pulling together weather, calendar, recent messages, and news into one readable summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to request a compact daily digest that combines weather, calendar, messages, and news into a readable Markdown briefing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may access upcoming calendar events and recent unread or important messages when used.

Mitigation: Invoke it explicitly and avoid recurring runs unless the user is comfortable with scheduled access to those sources.

Risk: News, weather, calendar, or message tools may be unavailable or incomplete.

Mitigation: Skip unavailable sections gracefully and make the briefing reflect only the available sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/daily-briefing)
- [Publisher profile](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown briefing with sections for time, weather, calendar, messages, and news]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Aims for a concise summary under 400 words and skips sections gracefully when tools are unavailable.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
