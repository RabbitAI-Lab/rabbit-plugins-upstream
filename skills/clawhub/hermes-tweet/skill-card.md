## Description: <br>
Hermes Tweet uses Xquik from Hermes Agent for X research, monitoring, and approval-gated X/Twitter actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xquik](https://clawhub.ai/user/xquik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, social teams, and agents use Hermes Tweet in Hermes Agent sessions to discover catalog-listed Xquik routes, read X/Twitter data, monitor topics, and prepare controlled account actions with explicit approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: X/Twitter actions can affect real accounts or workflow state. <br>
Mitigation: Keep HERMES_TWEET_ENABLE_ACTIONS unset or false unless an operation is intentionally approved, and summarize the endpoint, payload, account, reason, and side effects before calling action tooling. <br>
Risk: Secrets could be exposed if API keys are pasted into chat or tool arguments. <br>
Mitigation: Ask users to configure XQUIK_API_KEY in the Hermes runtime environment, never request or echo key values, and do not pass credentials in tool arguments. <br>
Risk: Guessed or direct endpoints could bypass the catalog and approval boundary. <br>
Mitigation: Use tweet_explore first, allow only catalog-listed Xquik API routes, and avoid direct HTTP fallbacks. <br>


## Reference(s): <br>
- [Hermes Tweet on ClawHub](https://clawhub.ai/xquik/skills/hermes-tweet) <br>
- [Endpoint and Approval Contract](references/endpoint-contract.md) <br>
- [Xquik Hermes Tweet Guide](https://docs.xquik.com/guides/hermes-tweet) <br>
- [Hermes Agent Plugin Guide](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/plugins.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Concise Markdown with JSON-like Hermes Tweet tool payloads and occasional shell commands for plugin checks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include endpoint selections, API-result summaries, action previews, and troubleshooting guidance; write-like actions require explicit approval.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
