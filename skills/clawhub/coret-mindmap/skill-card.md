## Description: <br>
Create, inspect, update, illustrate, export, and share live mind maps in coret.id through its MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ramaaditya49](https://clawhub.ai/user/ramaaditya49) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and workspace operators use this skill to create structured Coret mind maps from notes, meetings, research, plans, or outlines, and to inspect or update existing maps, nodes, drawings, sketches, exports, and share links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live Coret workspace data when connected with a live API key. <br>
Mitigation: Use a test key while trying workflows, switch to a live key only for intended production changes, and confirm the target workspace before live writes. <br>
Risk: Delete and batch update operations can remove nodes, descendants, or unrelated branches if used on the wrong target. <br>
Mitigation: Read the current map first, summarize affected branches before destructive batch operations, and require explicit confirmation for deletions. <br>
Risk: Public share links can expose map content beyond the workspace. <br>
Mitigation: Create share links only when requested and state the permission and expiry when a link is created. <br>
Risk: API keys could be exposed if copied into prompts, map content, logs, URLs, or share links. <br>
Mitigation: Never print, store, commit, or place the Coret API key in user-visible content, URLs, logs, or generated maps. <br>


## Reference(s): <br>
- [Coret Mind Map ClawHub listing](https://clawhub.ai/ramaaditya49/skills/coret-mindmap) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text responses describing Coret MCP tool actions, map IDs, summaries, exports, and share URLs when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce live Coret workspace changes through connected MCP tools; public share links are created only when requested.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
