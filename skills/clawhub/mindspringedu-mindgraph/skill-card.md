## Description: <br>
MindGraph diagrams from a topic plus diagram type (8 Thinking Maps, mind map, or concept map), or precise node text edits via PATCH. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lycosa9527](https://clawhub.ai/user/lycosa9527) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate MindGraph diagrams from a topic and diagram type, export diagram images, and make targeted node-label edits through the MindGraph API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose MindGraph credentials if users paste API tokens or account details into chat or logs. <br>
Mitigation: Configure MINDGRAPH_TOKEN and MINDGRAPH_ACCOUNT through environment or secret settings, never print the token, and regenerate the token if it was pasted into chat. <br>
Risk: Signed PNG URLs and generated diagram content may be shared outside the local conversation if forwarded. <br>
Mitigation: Treat image URLs and generated diagrams as user data, share only with intended recipients, and fetch a fresh image after edits instead of reusing stale links. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lycosa9527/skills/mindspringedu-mindgraph) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/lycosa9527) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, JSON, Configuration, Files] <br>
**Output Format:** [Markdown guidance with JSON request examples and API-produced PNG image links or files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MINDGRAPH_BASE_URL, MINDGRAPH_ACCOUNT, and MINDGRAPH_TOKEN environment variables; some PNG routes may require long HTTP timeouts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
