## Description: <br>
Moa Engine helps an agent decompose complex requests into a staged virtual expert-team workflow with specialist proposals, structured critique, revision, and a synthesized final answer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kiwifruit13](https://clawhub.ai/user/kiwifruit13) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they need deeper analysis, technical design, product planning, creative ideation, or other complex work broken into expert subproblems and reconciled into one final answer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The staged expert-and-critic workflow can be unnecessarily verbose or heavy for simple, single-domain requests. <br>
Mitigation: Use the MoA protocol only for complex tasks; answer directly when the user's request is simple or narrow. <br>
Risk: The skill is optimized for Chinese-language structured analysis, which may not match every user's preferred language or level of detail. <br>
Mitigation: Adapt the response language and depth to the user's request, and summarize staged reasoning when a shorter answer is more useful. <br>
Risk: Synthesized expert-role output can sound authoritative even when it is based on assumptions or incomplete evidence. <br>
Mitigation: Mark assumptions, preserve uncertainty, and review high-impact recommendations before relying on them. <br>


## Reference(s): <br>
- [MoA System Guide](references/moa-system-guide.md) <br>
- [MoA Meta Prompt](references/moa-meta-prompt.md) <br>
- [MoA Case Study](references/moa-case-study.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown response with staged expert, critic, revision, decision, and final-answer sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompt-only skill; optimized for verbose Chinese-language structured analysis unless adapted by the agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
