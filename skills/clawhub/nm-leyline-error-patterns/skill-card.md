## Description: <br>
Provides error classification, recovery, and graceful-degradation patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to classify service and agent failures, choose recovery strategies such as backoff or graceful degradation, and produce user-actionable error handling guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Full-context error logs can capture tokens, credentials, prompts, file paths, or personal data. <br>
Mitigation: Redact or minimize logs and alerts before applying the examples; avoid storing credentials or sensitive prompt content in debugging records. <br>
Risk: Generic error-handling patterns may be copied into a service without matching its reliability or escalation requirements. <br>
Mitigation: Review the classifications, retry limits, fallback behavior, and escalation paths before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-leyline-error-patterns) <br>
- [Leyline Plugin Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; examples should be adapted and reviewed before use.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
