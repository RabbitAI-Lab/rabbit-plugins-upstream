## Description: <br>
Create, inspect, update, illustrate, export, and share live mind maps in coret.id through Coret MCP tools for notes, meetings, research, plans, outlines, or existing Coret map workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ramaaditya49](https://clawhub.ai/user/ramaaditya49) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn notes, meetings, research, plans, or outlines into Coret mind maps and to inspect, update, export, or share existing Coret maps through the Coret MCP connection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change Coret mind maps through the connected Coret MCP account. <br>
Mitigation: Use a test API key for trials and verify the target workspace before live writes. <br>
Risk: Deletion and batch update workflows can remove maps, nodes, or descendant branches. <br>
Mitigation: Require explicit confirmation for deletion and summarize affected branches before destructive batch operations. <br>
Risk: Public share links can expose map content outside the workspace. <br>
Mitigation: Create share links only when requested and state the permission and expiry. <br>
Risk: A Coret API key could be exposed if copied into prompts, logs, URLs, maps, or share links. <br>
Mitigation: Never print, store, commit, or place the API key in generated content or URLs. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown summaries with Coret MCP tool actions and exported JSON, Markdown, or text when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a connected Coret MCP server and CORET_API_KEY; public share links are created only when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
