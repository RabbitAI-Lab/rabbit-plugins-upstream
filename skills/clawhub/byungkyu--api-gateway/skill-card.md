## Description: <br>
Connect to external services through Maton-managed API routes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to Maton-managed routes for user-approved, app-specific reads and changes across supported SaaS services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can operate Maton-connected SaaS accounts, including services that may affect data, billing, administration, or communications. <br>
Mitigation: Review each requested connection and OAuth scope, start with read-only checks, and require explicit confirmation before any write, send, delete, billing, or admin action. <br>
Risk: Triggers or configured destinations can forward future data automatically until removed. <br>
Mitigation: Review trigger destinations before enabling them and remove connections or triggers when they are no longer needed. <br>
Risk: API keys and provider-issued tokens may be exposed through logs, prompts, shared files, or forwarded configuration. <br>
Mitigation: Keep credentials in memory or environment variables only, send them only to the expected Maton API host, and rotate any key that may have been exposed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/api-gateway) <br>
- [Maton Homepage](https://maton.ai) <br>
- [Maton API Reference](https://www.maton.ai/docs/api-reference) <br>
- [Maton CLI Manual](https://cli.maton.ai/manual) <br>
- [Supported Service References](references/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, API calls, Configuration] <br>
**Output Format:** [Markdown with inline shell, Python, URL, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, Maton account setup, and explicit user approval before non-GET requests.] <br>

## Skill Version(s): <br>
1.0.138 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
