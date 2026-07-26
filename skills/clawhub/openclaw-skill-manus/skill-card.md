## Description: <br>
Manus AI Skill for OpenClaw connects agents to the Manus API for autonomous research, software development, workflow automation, media generation, file upload, project management, status checks, and webhook notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[disi3r](https://clawhub.ai/user/disi3r) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to delegate research, development, automation, file-processing, and content-generation tasks to Manus through command-line scripts and API calls. It is intended for workflows where an OpenClaw agent needs a long-running external autonomous agent and can safely provide prompts, files, or connected-account context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill delegates broad autonomous actions to an external Manus service that may interact with connected accounts such as Gmail, Notion, Google Calendar, and Slack. <br>
Mitigation: Use least-privilege or test accounts and require explicit human confirmation before bookings, posts, calendar changes, or other account mutations. <br>
Risk: Prompts and uploaded files are sent to an external API and may include sensitive user, business, or regulated data. <br>
Mitigation: Avoid uploading secrets or regulated data, minimize shared context, and review prompts and files before submitting tasks. <br>
Risk: The included webhook server listens on all interfaces and the security guidance warns against public exposure without added controls. <br>
Mitigation: Keep the webhook server private unless network restrictions and webhook authentication are added. <br>
Risk: Long-running autonomous tasks consume Manus credits and may continue after the local timeout. <br>
Mitigation: Set task timeouts and monitor status and credit usage before running broad or open-ended requests. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/disi3r/skills/openclaw-skill-manus) <br>
- [Publisher profile](https://clawhub.ai/user/disi3r) <br>
- [Manus homepage](https://manus.im) <br>
- [Manus API base URL](https://api.manus.ai/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples; scripts print JSON-derived task, project, file, webhook, and result information as terminal text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MANUS_API_KEY and sends prompts, uploaded files, task metadata, webhook registrations, and connected-account requests to the external Manus API.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
