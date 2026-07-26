## Description: <br>
Turn NxVET voice notes / button recordings into local reminders, calendar events (.ics), and a daily triage note on the user's own machine, with no send paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[talnirnx](https://clawhub.ai/user/talnirnx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, operators, and agent-assisted developers use this skill to build a local NxVET voice-note poller that turns spoken reminders into reviewable triage notes and calendar files. It is intended for organizations with an NxVET API key and an NxHUB device. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The NxVET API key may allow access to organization data. <br>
Mitigation: Store the key only in .env or the runtime environment, mask it in logs, keep it out of commits and shared channels, and revoke it from NxVET if exposed. <br>
Risk: Voice-note transcripts, state, and generated reminders can contain sensitive clinic or patient information. <br>
Mitigation: Keep .env, state, and output files local, git-ignored, and out of cloud sync unless the operator explicitly approves. <br>
Risk: Calendar or follow-up entries may be wrong if a transcript is ambiguous or a relative date is resolved incorrectly. <br>
Mitigation: Quote the original transcript in outputs, place unclear items in an Unclear section, and require the operator to review .ics files before adding them to a calendar. <br>
Risk: Adding outbound integrations would weaken the local-only privacy posture. <br>
Mitigation: Keep the normal release path to authenticated NxVET reads and local file creation; require explicit approval before adding email, calendar API, telemetry, or webhook send paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/talnirnx/skills/voice-notes-to-reminders) <br>
- [NxVET voice notes skill page](https://api.nx.vet/skills.html#voice-notes) <br>
- [NxVET API documentation](https://api.nx.vet/) <br>
- [NxVET full agent guide](https://api.nx.vet/llms-full.txt) <br>
- [NxVET OpenAPI specification](https://api.nx.vet/openapi/nxvet-api.yaml) <br>
- [NxVET MCP setup](https://api.nx.vet/mcp.html) <br>
- [NxHUB product page](https://nx.vet/products/nxhub) <br>
- [NxVET API reference notes](artifact/reference/nxvet-api.md) <br>
- [Security and privacy guidance](artifact/reference/security.md) <br>
- [Caching, state, and idempotency guidance](artifact/reference/caching-and-state.md) <br>
- [Good practices](artifact/reference/good-practices.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with Python scripts, JSON transcript output, markdown triage notes, and .ics calendar files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3 and NXVET_API_KEY; generated reminder state and outputs are local files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
