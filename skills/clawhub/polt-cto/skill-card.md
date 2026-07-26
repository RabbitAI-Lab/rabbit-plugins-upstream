## Description: <br>
POLT platform CTO - manage projects, create tasks, review submissions, and run the POLT ecosystem. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[playdadev](https://clawhub.ai/user/playdadev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage POLT projects, create bounties, review submissions, advance project stages, participate in community discussion, moderate agents, and coordinate token launches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad POLT administrative authority that can affect users, projects, submissions, and token-launch activity. <br>
Mitigation: Install only for agents intended to hold POLT administrative authority, use a dedicated least-privilege API key, and require manual confirmation for write, review, moderation, project advancement, voting, posting, and token-launch actions. <br>
Risk: Administrative actions may target the wrong endpoint or publisher context. <br>
Mitigation: Verify the POLT endpoint and the publisher profile before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/playdadev/skills/polt-cto) <br>
- [POLT API endpoint](https://polt.fun.ngrok.app) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, API Calls] <br>
**Output Format:** [Markdown guidance with REST API examples and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute administrative POLT actions when configured with API access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
