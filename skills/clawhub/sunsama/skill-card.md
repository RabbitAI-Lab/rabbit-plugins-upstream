## Description:

Helps agents manage Sunsama tasks, daily plans, calendars, objectives, time tracking, and linked email threads through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Sunsama can ask an agent to find and organize tasks, plan calendar time, track work, and manage linked email threads. With explicit approval, the agent can also set up related automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected tasks, calendar entries, and email threads may contain sensitive personal information.

Mitigation: Authorize only the needed access, return only information needed for the request, and avoid exposing raw responses or credentials.

Risk: Writes, deletions, email actions, and connection changes can alter or remove user data.

Mitigation: Prefer read-only actions and confirm the target and intended effect before each change.

Risk: Hosted functions, triggers, or destinations can perform ongoing actions or forward events.

Mitigation: Obtain explicit, separate approval for each automation and destination, including what it will do and where events will go.

Risk: Raw API keys can expose long-lived account access.

Mitigation: Prefer the CLI's OAuth login and avoid printing, logging, or sharing credentials.

## Reference(s):

- [Sunsama skill release](https://clawhub.ai/byungkyu/skills/sunsama)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Sunsama](https://sunsama.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with task or calendar details and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include information from the user's connected Sunsama account and linked email.]

## Skill Version(s):

1.2.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
