## Description: <br>
Install and use the RunAPI CLI as the universal execution layer for RunAPI models when an agent needs to run model tasks, inspect auth, install RunAPI, pass JSON request bodies, wait for tasks, or automate workflows from the terminal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agent operators use this skill to install, authenticate, inspect, and run RunAPI model workflows from terminals, servers, CI jobs, or supported agent runtimes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The curl-based installer can introduce supply-chain risk if used without review or artifact verification. <br>
Mitigation: Prefer the Homebrew installation path when available; for CI or server installs, review the fetched script first or pin and verify the release artifact independently. <br>
Risk: RunAPI credentials, callback signing secrets, and uploaded local media can be sensitive. <br>
Mitigation: Use environment variables or stdin for API keys, avoid logging listener secrets, keep credentials out of project config, and treat uploaded media URLs as temporary sensitive artifacts. <br>
Risk: Listener and cross-agent install commands can affect local services or other agent runtimes. <br>
Mitigation: Run listener or cross-agent install commands only when the workflow intentionally needs them, and select listener callback API key IDs explicitly in non-interactive contexts. <br>


## Reference(s): <br>
- [RunAPI model catalog and CLI documentation](https://runapi.ai/models.md) <br>
- [RunAPI models homepage](https://runapi.ai/models) <br>
- [ClawHub runapi-cli skill page](https://clawhub.ai/runapi-ai/skills/runapi-cli) <br>
- [ClawHub runapi-ai publisher profile](https://clawhub.ai/user/runapi-ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and TOML configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may produce JSON on stdout and progress or error messages on stderr when executed by the agent.] <br>

## Skill Version(s): <br>
0.2.14 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
