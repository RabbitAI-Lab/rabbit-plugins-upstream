## Description: <br>
Track every token and dollar your OpenClaw agent spends, set budget walls that actually refuse calls, and replay runs on free local models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shekharbhardwaj](https://clawhub.ai/user/shekharbhardwaj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to install and query a local Agentic Ledger proxy for OpenClaw cost, token, latency, budget, and replay reporting. It helps agents answer spend and usage questions from ledger data instead of estimates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local proxy records full prompts and responses on the user's machine, which can expose sensitive transcript data if the ledger storage is not protected. <br>
Mitigation: Review the ledger storage location and retention behavior before use, secure or delete local ledger data as appropriate, and avoid enabling it for highly sensitive work unless local transcript retention is acceptable. <br>


## Reference(s): <br>
- [Agentic Ledger on ClawHub](https://clawhub.ai/shekharbhardwaj/skills/agentic-ledger) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Analysis] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Plain-language cost and usage summaries based on local ledger API responses.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
