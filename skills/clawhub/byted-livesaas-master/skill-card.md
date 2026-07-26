## Description: <br>
Enterprise livestream / LiveSaaS control skill that helps an agent use the bytedlive CLI to manage livestream rooms, comments, system messages, audience controls, product cards, analytics, media operations, and OpenAPI fallback calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volcvneomnistreambot](https://clawhub.ai/user/volcvneomnistreambot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and livestream operations teams use this skill to let an agent set up LiveSaaS credentials, install or select the appropriate bytedlive CLI entry point, and perform enterprise livestream room, audience, comment, product, and analytics tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can grant an agent operational control over enterprise livestream resources, including room changes, messaging, moderation, and viewer management. <br>
Mitigation: Install only for trusted publishers and limit use to accounts and workspaces where the agent is authorized to operate LiveSaaS resources. <br>
Risk: The skill may install global npm CLI packages and use stored LiveSaaS credentials. <br>
Mitigation: Review package sources, run in a controlled environment, and use least-privilege credentials with local credential entry rather than sharing secrets in chat. <br>
Risk: The artifact includes startup usage reporting before the user's task proceeds. <br>
Mitigation: Review the telemetry behavior and disable it with BYTEDLIVE_TELEMETRY_DISABLED in enterprise or regulated environments when reporting is not approved. <br>
Risk: Deletion, blocking, kicking, and other moderation actions can affect livestream operations and users. <br>
Mitigation: Require explicit confirmation for destructive or high-impact actions and verify target room and viewer identifiers before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/volcvneomnistreambot/skills/byted-livesaas-master) <br>
- [Volcengine Enterprise Live API reference](https://www.volcengine.com/docs/3019/66792?lang=zh) <br>
- [Volcengine Enterprise Live API release history](https://www.volcengine.com/docs/3019/129183?lang=zh) <br>
- [OpenAPI action version data](references/data/openapiActionVersions.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI-generated JSON or tabular results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute npm installation, credential checks, remote login flows, bytedlive control commands, and OpenAPI calls through the CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact frontmatter states 1.1.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
