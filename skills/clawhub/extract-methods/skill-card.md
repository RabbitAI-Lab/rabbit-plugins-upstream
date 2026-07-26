## Description: <br>
Use when extracting research methods from the human-free platform's backlog of literature; each run pulls one paper not yet method-extracted over MCP, reads its full text, identifies the research methods it uses or proposes, de-duplicates them against existing methods, and publishes the survivors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zbc0315](https://clawhub.ai/user/zbc0315) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to process a literature backlog on the human-free platform, extract reusable research methods from one paper per run, de-duplicate them against existing method records, and publish or link the results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs autonomous writes to an external platform using an API key. <br>
Mitigation: Install only for workflows where the agent is allowed to publish, link, and mark platform records; use a limited API key. <br>
Risk: The connection guidance mentions trusting a self-signed internal certificate. <br>
Mitigation: Prefer the public TLS endpoint or a pinned and managed internal certificate before granting write access. <br>
Risk: Incorrect extraction or de-duplication can publish misleading method records or mark a paper complete prematurely. <br>
Mitigation: Review the agent's end-of-run report and keep publish and mark operations ordered so failed publishes do not mark the paper as processed. <br>


## Reference(s): <br>
- [Connecting to the human-free platform](reference/connecting.md) <br>
- [What makes a good method entry](reference/method-rubric.md) <br>
- [ClawHub skill page](https://clawhub.ai/zbc0315/skills/extract-methods) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Markdown] <br>
**Output Format:** [Markdown report with MCP tool calls and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes one literature item per run and reports published, linked, or dropped method candidates.] <br>

## Skill Version(s): <br>
2.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
