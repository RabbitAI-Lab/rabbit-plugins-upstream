## Description: <br>
Integrate Backboard.io for assistants, threads, memories, and document RAG via a local backend on http://localhost:5100. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrisk60331](https://clawhub.ai/user/chrisk60331) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to manage Backboard assistants, conversation threads, persistent memories, and document RAG workflows from an agent through a local backend. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security summary says the skill exposes a powerful Backboard backend that users should review before installing. <br>
Mitigation: Review before installing, use a dedicated Backboard API key, and require explicit confirmation before saving memories, uploading sensitive files, or deleting Backboard resources. <br>
Risk: The backend startup script binds the Flask service to 0.0.0.0 on port 5100. <br>
Mitigation: Bind the backend to 127.0.0.1 instead of 0.0.0.0 and avoid running it on untrusted networks. <br>
Risk: Dependencies are installed from the backend project at startup. <br>
Mitigation: Pin and audit dependencies before long-term use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrisk60331/skills/backboard) <br>
- [Publisher profile](https://clawhub.ai/user/chrisk60331) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API Calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON examples and local API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BACKBOARD_API_KEY and a local Flask backend on http://localhost:5100.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
