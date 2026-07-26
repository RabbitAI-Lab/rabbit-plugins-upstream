## Description: <br>
Restyle or relight an existing video, changing the whole frame's look while the motion carries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content-creation agents use this skill to choose between whole-frame video restyling and localized video edits, collect the required source clip and edit intent, and prepare asynchronous video-editing requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided video may be sent to external generation providers for processing. <br>
Mitigation: Avoid confidential, biometric, unreleased, or rights-restricted footage unless the user accepts provider processing. <br>
Risk: Routing ambiguity between whole-frame restyling and localized edits can produce broader visual changes than intended. <br>
Mitigation: Ask whether the whole frame should be reimagined or only one named element should change, then preserve untouched regions explicitly in the prompt. <br>
Risk: Video edits can drift from the requested appearance or preservation constraints. <br>
Mitigation: Review the returned video before delivery and retry with lower transform strength, a tighter preserve clause, or anchored reference frames when needed. <br>


## Reference(s): <br>
- [Edit video worked recipes](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, configuration] <br>
**Output Format:** [Markdown guidance with JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces asynchronous video-editing request guidance and result-handling steps for an agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
