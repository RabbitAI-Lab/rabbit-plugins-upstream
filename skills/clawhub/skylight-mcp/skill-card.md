## Description:

Read and manage your Skylight Calendar family hub — calendar events, chores and reward stars, shared lists (grocery/to-do), and meal plans. Triggers on phrases like "check Skylight", "what's on the family calendar", "add an event to Skylight", "what chores does [kid] have", "mark [chore] done", "add milk to the grocery list", "what's on our shopping list", "what's for dinner", "what's on the meal plan", "who's on the Skylight frame", or any request involving the Skylight frame, family calendar, chores, rewards, shared lists, or meals. Works against your own signed-in Skylight account via email + password.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Household members use the skill to check and update their Skylight family hub, including calendar events, chores and rewards, shared lists, meal plans, messages, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Everyday requests can trigger access to or changes in shared family information without making Skylight the intended service explicit.

Mitigation: Require explicit Skylight context for household reads and edits, or select Skylight as the default service before acting.

Risk: The connector uses account credentials and an external npm package; the security review covered the bundled instructions, not the external server executable.

Mitigation: Protect the credential-bearing configuration, keep user approval enabled, and review and pin the npm package version before use.

## Reference(s):

- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp on npm](https://www.npmjs.com/package/skylight-mcp)
- [Project source repository (listed in skill documentation)](https://github.com/chrischall/skylight-mcp)

## Skill Output:

**Output Type(s):** [text, structured data, API calls, configuration instructions]

**Output Format:** [Text responses and structured Skylight tool results; JSON configuration example]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can read and change household calendar, chores, lists, meal plans, and related family hub data. Some broader changes require user confirmation.]

## Skill Version(s):

1.5.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
