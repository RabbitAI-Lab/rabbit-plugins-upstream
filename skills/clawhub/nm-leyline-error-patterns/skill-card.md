## Description: <br>
Provides error classification, recovery, and graceful-degradation patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to classify failures, choose recovery strategies, and write user-actionable error handling guidance for resilient agent or plugin workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Logging and alerting examples may capture prompts, tokens, or sensitive service context if copied directly into production. <br>
Mitigation: Redact secrets, prompt content, and sensitive metadata before adopting the logging or alert examples. <br>
Risk: Agent recovery guidance discusses spawning replacement agents, reassigning work, and preserving commits. <br>
Mitigation: Keep spawning, reassignment, and commit behavior explicitly user-directed or governed by the orchestrator. <br>
Risk: Broad error-handling triggers could activate the skill during unrelated debugging work. <br>
Mitigation: Narrow triggers or require explicit invocation where accidental activation would disrupt the workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-error-patterns) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/athola) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Error classification module](modules/classification.md) <br>
- [Recovery strategies module](modules/recovery-strategies.md) <br>
- [Agent damage control module](modules/agent-damage-control.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown with Python and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-style reference output; no executable install code is included.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
