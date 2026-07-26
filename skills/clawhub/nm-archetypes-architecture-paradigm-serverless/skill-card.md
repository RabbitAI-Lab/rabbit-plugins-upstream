## Description: <br>
Applies serverless FaaS patterns for event-driven workloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and architects use this skill to evaluate when serverless FaaS patterns fit event-driven, bursty workloads and to plan state management, deployment, observability, cost, and risk considerations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Serverless architecture guidance may not match a user's deployment, IAM, cost, or compliance constraints. <br>
Mitigation: Validate recommendations against the target cloud environment, organizational policies, and workload requirements before acting. <br>
Risk: Long-running processes, persistent connections, and local state requirements can make a serverless FaaS design unsuitable. <br>
Mitigation: Check workload duration, connection, and state requirements before adopting serverless patterns. <br>
Risk: Cold starts, provider limits, and provider-specific APIs can affect latency, reliability, and portability. <br>
Mitigation: Plan cold-start mitigation, monitor provider quotas, and isolate provider-specific integrations where portability matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-serverless) <br>
- [Configured OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with architecture checklists and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable code; cloud deployment, IAM, cost, and compliance decisions should be validated against the user's own environment.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
