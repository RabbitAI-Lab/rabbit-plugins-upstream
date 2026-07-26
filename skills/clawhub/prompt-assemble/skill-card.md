## Description: <br>
Token-safe prompt assembly with memory orchestration for agents that need to construct LLM prompts with optional memory retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexunitario-sketch](https://clawhub.ai/user/alexunitario-sketch) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to assemble prompts with recent dialog and optional long-term memory while keeping memory injection bounded by token-budget checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Heuristic token estimates may be inaccurate near a model context limit. <br>
Mitigation: Validate token counts against the target model before relying on the helper close to context limits. <br>
Risk: Long-term memory can expose sensitive or stale user information if stored without governance. <br>
Mitigation: Use explicit user consent, review, deletion workflows, and sensitive-data limits for any long-term memory store. <br>


## Reference(s): <br>
- [Prompt Safe ClawHub page](https://clawhub.ai/alexunitario-sketch/skills/prompt-assemble) <br>
- [alexunitario-sketch publisher profile](https://clawhub.ai/user/alexunitario-sketch) <br>
- [Memory Data Standards](references/memory_standards.md) <br>
- [Token Estimation Strategies](references/token_estimation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python implementation code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces assembled prompt text through the included Python helper; memory is optional and may be skipped when the estimated prompt exceeds the configured safety threshold.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
