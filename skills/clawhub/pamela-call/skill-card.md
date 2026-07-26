## Description: <br>
Make AI phone calls instantly. No lag, no setup, unlimited scale. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eypam](https://clawhub.ai/user/eypam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent builders use this skill to help configure Pamela-powered outbound calls, phone tree navigation, webhooks, SDK usage, CLI usage, and MCP integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent place real outbound phone calls. <br>
Mitigation: Confirm the recipient, task, consent, legal basis, and any recording or AI disclosure duties before enabling live calling. <br>
Risk: Live API use can incur billing charges. <br>
Mitigation: Use a test or restricted key for trials, enable billing alerts, and monitor connected minutes before production use. <br>
Risk: The Pamela API key grants access to paid calling capabilities. <br>
Mitigation: Store PAMELA_API_KEY only in a secret manager or protected environment variable and avoid placing production keys in public configs or logs. <br>
Risk: Call audio, transcripts, and webhook payloads may contain sensitive information. <br>
Mitigation: Review transcript sensitivity, secure webhook endpoints, and validate the X-Pamela-Signature header before processing webhook events. <br>


## Reference(s): <br>
- [Pamela documentation](https://docs.thisispamela.com) <br>
- [JavaScript SDK documentation](https://docs.thisispamela.com/sdk/javascript) <br>
- [Webhook signature verification](https://docs.thisispamela.com/sdk/javascript#verifywebhooksignature) <br>
- [Python SDK documentation](https://docs.thisispamela.com/sdk/python) <br>
- [MCP server documentation](https://docs.thisispamela.com/sdk/mcp) <br>
- [CLI documentation](https://docs.thisispamela.com/sdk/cli) <br>
- [npm @thisispamela packages](https://www.npmjs.com/org/thisispamela) <br>
- [PyPI thisispamela package](https://pypi.org/project/thisispamela/) <br>
- [ClawHub skill page](https://clawhub.ai/eypam/skills/pamela-call) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell, TypeScript, and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PAMELA_API_KEY and an active Pamela API subscription for live calls.] <br>

## Skill Version(s): <br>
1.1.12 (source: server release evidence and artifact release note) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
