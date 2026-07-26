## Description: <br>
Generate and build Pulse Apps using the Vibe Dev Flow API when a user wants to create, update, or generate code for Pulse Editor applications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shellishack](https://clawhub.ai/user/shellishack) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI agents use this skill to call Pulse Editor's Vibe Dev Flow API to create new Pulse Apps, update existing apps, generate code, and receive published app artifacts without local build dependencies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pulse Editor API keys or other credentials could be exposed if placed directly in prompts, source files, or command history. <br>
Mitigation: Use a scoped API key or credential manager and avoid hardcoding secrets. <br>
Risk: Prompts sent to the Pulse Editor API may contain sensitive or regulated data. <br>
Mitigation: Avoid placing secrets or regulated data in prompts. <br>
Risk: The skill may update an existing app or publish a live generated app. <br>
Mitigation: Confirm before updating an existing app or publishing a live generated app. <br>


## Reference(s): <br>
- [Pulse Editor Documentation](https://docs.pulse-editor.com/) <br>
- [Pulse Editor API Reference](https://docs.pulse-editor.com/api-reference) <br>
- [Get a Pulse Editor API Key](https://docs.pulse-editor.com/api-reference/get-pulse-editor-api-key) <br>


## Skill Output: <br>
**Output Type(s):** [API calls, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with JSON, bash, Python, and TypeScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SSE streaming and requires a Pulse Editor API key. Final artifacts may include a published app link, source code archive link, appId, and version.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
