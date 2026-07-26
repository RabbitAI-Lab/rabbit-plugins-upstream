## Description: <br>
Helps QA and release teams design shift-right validation for production releases using canary monitoring, synthetic checks, A/B validation, user feedback, chaos engineering, alert thresholds, and rollback triggers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and release owners use this skill when a feature is live or entering canary release and they need a production validation plan covering monitoring, synthetic checks, feedback loops, chaos experiments, alerts, and rollback criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Production validation guidance could be mistaken for permission to change monitoring, rollout, or experiment settings. <br>
Mitigation: Use the skill only with release ownership and explicit approval for production monitoring, rollout changes, and chaos experiments. <br>
Risk: User behavior analysis or feedback collection could involve personal or sensitive data. <br>
Mitigation: Confirm consent, data handling requirements, and applicable privacy obligations before collecting or analyzing user data. <br>
Risk: Chaos experiments or canary releases can affect live users if the blast radius is too broad. <br>
Mitigation: Start in non-production, shadow, or narrowly scoped canary environments, then expand only with circuit breakers and rollback criteria in place. <br>
Risk: A production rollout plan without clear rollback thresholds can delay recovery from regressions. <br>
Mitigation: Define rollback triggers for error rate, latency, business metrics, and user feedback before rollout begins, and rehearse the rollback path. <br>


## Reference(s): <br>
- [Qa Shift Right on ClawHub](https://clawhub.ai/kokxi/skills/qa-shift-right) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown plan with monitoring metrics, synthetic checks, alert thresholds, rollback triggers, feedback loops, and traceability notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Planning guidance only; no production action is executed by the skill.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
