## Description: <br>
TensorPM helps agents manage projects, track action items, and coordinate teams through a local-first desktop app with MCP tools and A2A agent communication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[neo552](https://clawhub.ai/user/neo552) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, agents, and project teams use this skill to connect an AI client to TensorPM for project creation, action item tracking, workspace switching, and project-agent conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local TensorPM app can expose and change project data through an unauthenticated localhost A2A API when optional auth is not enabled. <br>
Mitigation: Enable A2A_HTTP_AUTH_TOKEN before starting TensorPM, and run it only on trusted local machines. <br>
Risk: Local agents and processes may interact with project content, imported files, and configured provider access. <br>
Mitigation: Install TensorPM only from trusted download channels and avoid placing highly sensitive project content, imported files, or API keys into the app unless that local-agent access is acceptable. <br>


## Reference(s): <br>
- [TensorPM homepage](https://tensorpm.com) <br>
- [ClawHub TensorPM skill page](https://clawhub.ai/neo552/skills/tensorpm) <br>
- [TensorPM release notes](https://github.com/Neo552/TensorPM-Releases/releases/latest) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the TensorPM desktop app to be running for MCP tools and A2A communication.] <br>

## Skill Version(s): <br>
1.1.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
