## Description: <br>
Async Python patterns via asyncio and aiohttp for I/O-bound concurrency. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to apply asyncio and aiohttp patterns for concurrent I/O, web APIs, web scraping, async database work, timeouts, cancellation, and async testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Async code suggestions can introduce hanging operations, unbounded concurrency, or blocking calls in event-loop code. <br>
Mitigation: Review generated changes for timeouts, cancellation handling, semaphores or rate limits, and avoidance of blocking calls before deployment. <br>
Risk: Operational use in workspaces with sensitive credentials or production systems can expand the impact of agent-proposed commands or code changes. <br>
Mitigation: Install only in intended workspaces and keep destructive commands, outbound communications, production deploys, and shared memory writes under explicit human approval. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-parseltongue-python-async) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/parseltongue) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
