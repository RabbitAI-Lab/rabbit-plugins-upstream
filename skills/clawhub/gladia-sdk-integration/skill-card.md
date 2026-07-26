## Description: <br>
Helps agents install, configure, and choose the official Gladia JavaScript/TypeScript and Python SDKs for speech-to-text integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gladiaio](https://clawhub.ai/user/gladiaio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill when adding Gladia speech-to-text SDK support to JavaScript, TypeScript, or Python applications. It guides SDK installation, client initialization, API key and region setup, browser proxy patterns, retry and timeout configuration, and SDK-versus-raw-API decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys can be exposed if embedded in browser-side code. <br>
Mitigation: Keep API keys server-side where possible and use a backend proxy for browser applications. <br>
Risk: Speech-to-text workflows may send user audio to Gladia. <br>
Mitigation: Make audio capture opt-in with visible start and stop controls, and disclose that audio is sent to Gladia. <br>
Risk: Delete operations can remove remote jobs or sessions. <br>
Mitigation: Require clear user confirmation before deleting remote jobs or sessions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gladiaio/skills/gladia-sdk-integration) <br>
- [SDK integration guide](https://docs.gladia.io/chapters/integrations/sdk) <br>
- [JavaScript SDK on npm](https://www.npmjs.com/package/@gladiaio/sdk) <br>
- [Python SDK on PyPI](https://pypi.org/project/gladiaio-sdk/) <br>
- [SDK source code](https://github.com/gladiaio/sdk) <br>
- [Code samples](https://github.com/gladiaio/gladia-samples) <br>
- [Current SDK versions](references/sdk-versions.md) <br>
- [Client configuration reference](references/client-config.md) <br>
- [JavaScript and TypeScript SDK patterns](references/javascript.md) <br>
- [Python SDK patterns](references/python.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code snippets, install commands, configuration examples, and reference links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Language-specific guidance for JavaScript/TypeScript and Python SDK setup, including runtime requirements, API key handling, retry and timeout configuration, and error-handling patterns.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
