## Description: <br>
Posthive helps agents draft, schedule, approve, update, list, and delete social media posts across 13 platforms through the Posthive CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[astablackclove](https://clawhub.ai/user/astablackclove) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage social media publishing workflows from an agent by creating drafts, scheduling posts, approving queued content, and managing existing posts through explicit Posthive CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Posthive CLI can access connected social accounts and stores local login credentials. <br>
Mitigation: Install only when the publisher and Posthive account access are trusted, and prefer scoped API keys or logged-in accounts appropriate for the publishing task. <br>
Risk: Approve, schedule, update, and delete commands can affect public social media content. <br>
Mitigation: Default to drafts, review generated content before approval, confirm target account IDs, and verify timezone and ISO 8601 UTC schedule values before execution. <br>


## Reference(s): <br>
- [Server-resolved source provenance](https://github.com/AstaBlackClove/posthive/tree/main/apps/cli/skills/posthive) <br>
- [ClawHub Posthive skill page](https://clawhub.ai/astablackclove/skills/posthive-mcp) <br>
- [Posthive API service endpoint](https://api.posthive.co) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; referenced CLI commands output structured JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may use a browser login or POSTHIVE_API_KEY; scheduled timestamps are ISO 8601 UTC.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
