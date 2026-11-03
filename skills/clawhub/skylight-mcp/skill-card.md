## Description:

Read and manage your Skylight Calendar family hub — calendar events, chores and reward stars, shared lists (grocery/to-do), and meal plans. Triggers on phrases like "check Skylight", "what's on the family calendar", "add an event to Skylight", "what chores does [kid] have", "mark [chore] done", "add milk to the grocery list", "what's on our shopping list", "what's for dinner", "what's on the meal plan", "who's on the Skylight frame", or any request involving the Skylight frame, family calendar, chores, rewards, shared lists, or meals. Works against your own signed-in Skylight account via email + password.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Families and their assistants can use the skill to check and update a signed-in Skylight family hub, including its calendar, chores, shared lists, meals, and frame settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector is an external package with access to the user's Skylight family account.

Mitigation: Install only a package release you trust and consider pinning a reviewed version; the bundled instructions were reviewed, but the npm runtime and its enforcement were not fully audited.

Risk: Email and password credentials are required, and account configuration could expose them if shared or committed.

Mitigation: Protect credential configuration from sharing or source control, and keep user confirmation controls enabled for gated changes.

Risk: Ambiguous requests can target the wrong frame or list, and some changes may affect future occurrences or other people.

Mitigation: Specify Skylight and the intended frame or list; review confirmation previews before approving wider-scope changes or invitations.

## Reference(s):

- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured Skylight tool results and natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reflect calendar, family, and account data or requested changes.]

## Skill Version(s):

1.4.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
