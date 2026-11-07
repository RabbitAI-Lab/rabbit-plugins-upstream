## Description:

Read and manage your Skylight Calendar family hub — calendar events, chores and reward stars, shared lists (grocery/to-do), and meal plans. Triggers on phrases like "check Skylight", "what's on the family calendar", "add an event to Skylight", "what chores does [kid] have", "mark [chore] done", "add milk to the grocery list", "what's on our shopping list", "what's for dinner", "what's on the meal plan", "who's on the Skylight frame", or any request involving the Skylight frame, family calendar, chores, rewards, shared lists, or meals. Works against your own signed-in Skylight account via email + password.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Families and household members use this skill to check and manage their Skylight Calendar frame, including events, chores, rewards, shared lists, and meal plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad request triggers may activate the skill for loosely scoped Skylight requests.

Mitigation: Check that the request concerns the user's connected family frame and intended task before using a tool.

Risk: The setup uses the user's Skylight email and password to access their account.

Mitigation: Keep credentials in the MCP environment configuration and do not ask the user to share passwords in chat.

Risk: Some operations can change shared data, access, or affect people outside the frame.

Mitigation: Honor the documented confirmation gates and show the preview before carrying out a gated change.

Risk: The security review reports partial Skillspector coverage because two local references were unresolved.

Mitigation: Review the setup and relevant skill material before deployment, accounting for the incomplete scan coverage.

## Reference(s):

- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp on npm](https://www.npmjs.com/package/skylight-mcp)
- [Project repository linked in the skill documentation](https://github.com/chrischall/skylight-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data, Guidance]

**Output Format:** [Natural-language summaries and structured Skylight records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results and changes are scoped to a selected or automatically resolved family frame.]

## Skill Version(s):

1.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
