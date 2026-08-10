## Description: <br>
Gives AI agents persistent memory for content ideas and drafts through BlueColumn storage, note, and recall API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content-creation teams use this skill to let an agent store, search, and recall content ideas or draft context across interactions with a BlueColumn API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Content ideas, drafts, and interaction summaries may be sent to BlueColumn for persistent memory without clear user approval, limits, or deletion guidance. <br>
Mitigation: Use only with user-approved, non-confidential content and establish consent, retention, and deletion practices before storing content. <br>
Risk: The skill requires a BlueColumn API key and sends requests to external BlueColumn endpoints. <br>
Mitigation: Store the API key in the platform secret store, avoid embedding it in prompts or files, and review outbound requests before enabling the skill. <br>


## Reference(s): <br>
- [BlueColumn API Reference](https://bluecolumn.ai/docs) <br>
- [ClawHub Skill Page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/content-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown instructions with inline bash curl examples and API request guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key; stores and recalls text, query, title, and tag fields through BlueColumn endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
