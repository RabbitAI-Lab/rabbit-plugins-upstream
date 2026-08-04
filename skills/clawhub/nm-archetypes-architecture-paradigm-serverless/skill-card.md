## Description: <br>
Applies serverless FaaS patterns for event-driven workloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and architecture teams use this skill to evaluate when serverless FaaS patterns fit event-driven, variable-traffic workloads and to plan adoption steps, deliverables, and operational controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate during broad architecture discussions and provide guidance outside the user's intended design scope. <br>
Mitigation: Confirm that the workload is event-driven, variable in traffic, and appropriate for serverless constraints before applying recommendations. <br>
Risk: Generated IaC, deployment, or cloud permission changes could affect infrastructure, cost, or access controls if applied without review. <br>
Mitigation: Review proposed IaC, CI/CD, IAM, observability, and budget changes separately before deployment. <br>
Risk: Serverless designs can introduce vendor lock-in, debugging complexity, cold-start latency, and resource-limit constraints. <br>
Mitigation: Use portable abstractions where feasible, instrument functions with tracing and structured logs, plan cold-start mitigation, and monitor provider limits. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-serverless) <br>
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration] <br>
**Output Format:** [Markdown prose with architecture recommendations, adoption steps, risk notes, and implementation checklists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ADR, IaC, CI/CD, observability, security, and cost-control guidance for serverless workloads.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
