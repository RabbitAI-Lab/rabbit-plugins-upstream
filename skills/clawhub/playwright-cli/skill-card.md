## Description: <br>
Playwright CLI helps agents drive browser sessions for web testing, page interaction, screenshots, network routing, storage inspection, and Playwright test generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to automate browser workflows, debug web applications, inspect page state, and turn specification-driven scenarios into Playwright tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can expose authenticated sessions, auth tokens, cookies, saved state, traces, screenshots, videos, and network logs. <br>
Mitigation: Use test accounts where possible, avoid production authenticated sessions, and treat generated browser artifacts and storage exports as secrets. <br>
Risk: The skill supports arbitrary browser-side code execution through commands such as run-code and eval. <br>
Mitigation: Review any script before execution and require explicit confirmation before running code that reads credentials, tokens, or sensitive page data. <br>
Risk: Persistent profiles and destructive session commands can retain or remove browser state across runs. <br>
Mitigation: Require explicit confirmation before persistent profile use, token extraction, kill-all, close-all, or delete-data commands. <br>


## Reference(s): <br>
- [Command Reference](references/commands.md) <br>
- [Usage Examples](references/examples.md) <br>
- [Specification-Driven Testing](references/spec-testing.md) <br>
- [Playwright Documentation](https://playwright.dev) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and Playwright TypeScript snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce screenshots, PDFs, traces, videos, snapshots, cookies, storage values, and network request details through Playwright CLI commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
