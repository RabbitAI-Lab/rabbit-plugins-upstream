## Description: <br>
Build a chat, reasoning, or tool-calling agent on top of Runware-hosted LLMs using OpenAI-compatible chat completions and tool-calling loops. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build Runware-hosted conversational, reasoning, or tool-calling agents over their own functions and APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides agents to call an external Runware API and user-defined functions, which can expose sensitive or destructive capabilities if broad tools are provided. <br>
Mitigation: Keep tool schemas narrow, validate parsed arguments, and add approval controls before exposing sensitive or destructive actions. <br>
Risk: Unbounded tool-calling loops can continue longer than intended or repeat failed actions. <br>
Mitigation: Cap loop iterations and return clear tool error objects so the model can adjust or stop. <br>
Risk: Stale model assumptions can lead to unsupported parameters or model selections. <br>
Mitigation: Confirm each model is live and inspect the current schema before making calls. <br>


## Reference(s): <br>
- [LLM agent worked recipes](artifact/references/examples.md) <br>
- [Runware OpenAI-compatible API endpoint](https://api.runware.ai/v1) <br>
- [ClawHub skill page](https://clawhub.ai/runware/skills/llm-agent) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Configuration] <br>
**Output Format:** [Markdown guidance with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; generated agent integrations should be checked against live Runware model schemas before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
