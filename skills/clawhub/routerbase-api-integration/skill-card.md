## Description: <br>
Integrates applications with RouterBase as an OpenAI-compatible model gateway for migration, API key setup, chat completions, streaming, tool calling, JSON mode, vision inputs, validation, error handling, and setup documentation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenlee123](https://clawhub.ai/user/zenlee123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to migrate or create OpenAI-compatible integrations that call RouterBase, configure ROUTERBASE_API_KEY server-side, and produce concise, testable examples for supported clients and frameworks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RouterBase API keys could be exposed if copied into browser, mobile, logs, or public repository code. <br>
Mitigation: Keep ROUTERBASE_API_KEY only in server-side environment variables and use placeholders in examples and documentation. <br>
Risk: Model availability, access, or pricing may change before production use. <br>
Mitigation: Check model IDs and pricing against RouterBase's live catalog before deployment. <br>


## Reference(s): <br>
- [RouterBase API Reference Notes](references/routerbase-api.md) <br>
- [RouterBase](https://routerbase.com) <br>
- [RouterBase Documentation](https://docs.routerbase.com) <br>
- [RouterBase Chat Completions API](https://docs.routerbase.com/api-reference/chat-completions) <br>
- [ClawHub Skill Page](https://clawhub.ai/zenlee123/skills/routerbase-api-integration) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline code blocks and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run validation steps and reminders to verify model availability and pricing against the live RouterBase catalog.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
