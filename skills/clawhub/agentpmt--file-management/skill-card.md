## Description: <br>
File Management lets agents upload, list, retrieve, share, download, delete, and manage files in AgentPMT cloud storage through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill when an agent needs budget-scoped cloud file storage, signed upload and download URLs, sharing, deletion, metadata management, or access-history inspection through AgentPMT. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Permanent deletion can remove the wrong stored file if the agent uses an incorrect file_id. <br>
Mitigation: Confirm the exact file_id before using the delete action. <br>
Risk: Shared links and signed download URLs can expose uploaded content to anyone who receives the link and satisfies the password constraints. <br>
Mitigation: Avoid uploading secrets unless the AgentPMT setup, retention, and sharing constraints are appropriate for the data. <br>


## Reference(s): <br>
- [ClawHub File Management Skill](https://clawhub.ai/agentpmt/skills/file-management) <br>
- [AgentPMT File Management Marketplace](https://www.agentpmt.com/marketplace/file-management) <br>
- [Schema Reference](artifact/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON call examples and schema tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes AgentPMT file lifecycle actions, action parameters, signed URL handling, and response handling guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
