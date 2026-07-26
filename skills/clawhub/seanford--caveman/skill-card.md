## Description: <br>
Caveman turns agent responses into an ultra-compressed communication style while preserving technical accuracy and supporting multiple intensity levels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and other agent users use this skill when they want concise, token-efficient responses for technical work while preserving exact code, API names, error strings, and substantive guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent terse mode can remain active after broad prompts such as "be brief" or "less tokens," which may surprise users who expect normal prose later. <br>
Mitigation: Use "normal mode" or "stop caveman" to turn it off, and install the skill only when persistent terse responses are desired. <br>
Risk: Compression can make nuanced warnings, irreversible actions, or multi-step ordering harder to read. <br>
Mitigation: Rely on the skill's documented auto-clarity behavior for security warnings, irreversible confirmations, and ambiguous sequences; ask for clarification or normal mode when precision matters. <br>
Risk: Wenyan modes can reduce readability for users who do not want Classical Chinese-style output. <br>
Mitigation: Use wenyan modes only when explicitly requested. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/seanford/skills/caveman) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or plain text responses, with code blocks unchanged when present] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Applies persistent terse style levels; code, command names, API names, and error strings remain exact.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
