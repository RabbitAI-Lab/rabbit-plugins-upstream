## Description: <br>
Diagnose and fix excessive Postgres egress (network data transfer) in a codebase. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrelandgraf](https://clawhub.ai/user/andrelandgraf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to find application queries that transfer excessive data from Postgres, reduce overfetching, add pagination or caching, and verify that egress drops without breaking API responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Query or API changes may alter response shape or omit fields that clients still depend on. <br>
Mitigation: Review proposed changes before production use, run existing tests, and confirm API response compatibility after column selection or pagination changes. <br>
Risk: Database statistics and cost findings may be unrepresentative if collected from an idle, recently reset, or non-production workload. <br>
Mitigation: Use the intended project and database, collect representative traffic before acting on statistics, and compare measurements after fixes. <br>
Risk: Neon branch configuration changes can affect non-production compute behavior and lifecycle. <br>
Mitigation: Apply configuration only to intended branches and review branch policy changes before deployment. <br>


## Reference(s): <br>
- [Neon Parent Skill](https://neon.com/docs/ai/skills/neon/SKILL.md) <br>
- [Neon Network Transfer Documentation](https://neon.com/docs/introduction/network-transfer.md) <br>
- [Neon Cost Optimization Documentation](https://neon.com/docs/introduction/cost-optimization.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/andrelandgraf/skills/neon-postgres-egress-optimizer) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with SQL, shell, and TypeScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include query diagnostics, code change recommendations, pagination or caching guidance, Neon branch configuration, and verification steps.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
