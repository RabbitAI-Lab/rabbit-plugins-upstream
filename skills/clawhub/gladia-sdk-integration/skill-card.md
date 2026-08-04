## Description: <br>
Install and configure the official Gladia SDKs (@gladiaio/sdk for JS/TS, gladiaio-sdk for Python). Use when the user asks about SDK setup, client initialization, API key configuration, choosing between JS and Python, browser usage, retry/timeout settings, error handling, or SDK vs raw API decisions. The SDK is the recommended default for all Gladia integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gladiaio](https://clawhub.ai/user/gladiaio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to install, configure, and choose the Gladia JavaScript/TypeScript or Python SDK for speech-to-text integrations, including API key, region, retry, timeout, browser proxy, and error-handling setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Gladia API keys can be exposed if copied into browser-side code. <br>
Mitigation: Keep API keys server-side and use a backend proxy for browser integrations. <br>
Risk: Audio may be sent to Gladia without proper rights or consent. <br>
Mitigation: Obtain consent before microphone capture and submit only audio files or URLs the user is allowed to share with Gladia. <br>
Risk: Runtime or dependency mismatches can cause SDK failures, especially Node.js WebSocket support and Python async usage. <br>
Mitigation: Use Node.js 20+ or Bun, install ws for Node.js versions before 22 when live sessions are needed, use Python 3.10+, and match sync or async clients to the application runtime. <br>


## Reference(s): <br>
- [Full Client Configuration Reference](references/client-config.md) <br>
- [JavaScript / TypeScript SDK](references/javascript.md) <br>
- [Python SDK](references/python.md) <br>
- [SDK Versions](references/sdk-versions.md) <br>
- [Gladia SDK integration guide](https://docs.gladia.io/chapters/integrations/sdk) <br>
- [@gladiaio/sdk on npm](https://www.npmjs.com/package/@gladiaio/sdk) <br>
- [gladiaio-sdk on PyPI](https://pypi.org/project/gladiaio-sdk/) <br>
- [Gladia SDK source code](https://github.com/gladiaio/sdk) <br>
- [Gladia code samples](https://github.com/gladiaio/gladia-samples) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JavaScript/TypeScript or Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no tools or API calls are executed by the skill itself.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
