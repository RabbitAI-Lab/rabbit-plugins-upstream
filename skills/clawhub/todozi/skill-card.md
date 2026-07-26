## Description: <br>
Todozi Eisenhower matrix API client + LangChain tools. Create matrices, tasks, goals, notes; list/search/update; bulk operations; webhooks. Categories: do, done, dream, delegate, defer, dont. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bgengs](https://clawhub.ai/user/bgengs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to connect agents to Todozi for creating, listing, searching, updating, completing, and deleting tasks, goals, notes, matrices, and webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access and modify a user's Todozi account. <br>
Mitigation: Install only when agent access to Todozi is intended, and use a scoped Todozi API key if available. <br>
Risk: Delete, completion, and bulk operations can change multiple Todozi records. <br>
Mitigation: Require user confirmation before deletes, completions, or bulk changes. <br>
Risk: A custom TODOZI_BASE endpoint could receive credentials or account actions. <br>
Mitigation: Leave TODOZI_BASE unset or set it only to an endpoint the user explicitly trusts. <br>
Risk: Webhook creation can send Todozi events to external URLs. <br>
Mitigation: Create webhooks only for HTTPS URLs the user controls or explicitly trusts. <br>


## Reference(s): <br>
- [Todozi API Reference](references/api_reference.md) <br>
- [Todozi API](https://todozi.com/api) <br>
- [ClawHub skill page](https://clawhub.ai/bgengs/skills/todozi) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with Python and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Todozi API key and can perform account-changing API operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
