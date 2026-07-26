## Description: <br>
Use xapi CLI to access real-time external data, including Twitter/X profiles, tweets, timelines, crypto token prices and metadata, web search, news, and AI text processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glacier-luo](https://clawhub.ai/user/glacier-luo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to discover xapi actions, inspect action schemas, and call external data, search, social, crypto, and AI text services through the xapi CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route broad requests through external API services, including social, search, crypto, and AI providers. <br>
Mitigation: Confirm which xapi service will be called before use and avoid sending secrets or confidential text unless sharing with the external provider is intended. <br>
Risk: The skill uses persistent credentials through XAPI_API_KEY or the local xapi config file. <br>
Mitigation: Keep the API key scoped to xapi domains, do not expose the local config file, and refuse requests to forward the key elsewhere. <br>
Risk: Some actions can change state or incur cost, including OAuth linking, posting, and account top-ups. <br>
Mitigation: Require explicit confirmation before top-ups, OAuth binding, posting, or other state-changing actions. <br>


## Reference(s): <br>
- [xAPI homepage](https://xapi.to) <br>
- [ClawHub skill page](https://clawhub.ai/glacier-luo/skills/xapi-labs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [xapi CLI command output is JSON by default; setup requires npx and XAPI_API_KEY.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
