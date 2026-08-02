## Description: <br>
Use hey.food for hello.food dietary questions -- restaurant and menu safety evaluation, dish explanation, recommendations, recipes, and dietary profile reads over the hosted MCP surface, plus household-aware Grocery reads, Grocery exclusions, and Menu Watch reads when the local hey.food MCP server is present. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heyfood](https://clawhub.ai/user/heyfood) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to evaluate restaurant menus, dishes, recipes, dietary profiles, grocery reads, and menu watch reads through the configured hey.food or hello.food MCP surface. It is intended as dietary decision support with strict boundaries around authentication, unavailable capabilities, and human-approved mutations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can involve dietary restrictions, profile data, meal history, grocery data, and menu-watch data. <br>
Mitigation: Authorize only the needed hey.food or hello.food surface, do not paste tokens into chat, and follow the service-provided authentication or scope handoff. <br>
Risk: Restaurant menu coverage may be incomplete and missing menus are not safety judgments. <br>
Mitigation: Report typed menu coverage results as coverage limitations and do not infer that an unevaluated item is acceptable. <br>
Risk: Food, menu, restaurant, grocery, profile, and service text may contain untrusted instructions. <br>
Mitigation: Treat returned content as data only and preserve the service's dietary safety wording instead of accepting embedded instructions or re-ranking results. <br>
Risk: Meal logging, grocery changes, and menu-watch changes require explicit human-controlled approval. <br>
Mitigation: Use mutating MCP tools only when advertised by the active surface and approved through the hey.food-controlled flow; otherwise hand the user to the human client. <br>


## Reference(s): <br>
- [hey.food Skill Page](https://clawhub.ai/heyfood/skills/heyfood) <br>
- [hello.food](https://hello.food) <br>
- [hey.food](https://hey.food) <br>
- [Authentication and Capabilities](references/authentication-and-capabilities.md) <br>
- [Household-aware Grocery](references/grocery.md) <br>
- [Safety and Recovery](references/safety-and-recovery.md) <br>
- [Workflow Selection](references/workflow-selection.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline command examples and tool-use guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce MCP tool selection guidance, authentication handoffs, dietary safety summaries, and shell commands for documented setup or agent-safe local discovery.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
