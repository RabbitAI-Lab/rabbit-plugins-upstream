## Description: <br>
Applies hexagonal architecture isolating domain from infrastructure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and software architects use this skill for guidance on applying hexagonal architecture, defining ports and adapters, and keeping domain logic isolated from infrastructure concerns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Architecture guidance may be over-applied to small utilities or prototypes where port and adapter abstractions add unnecessary overhead. <br>
Mitigation: Use the skill's when-not-to-use guidance and validate whether the system has enough external dependencies or testing needs to justify the pattern. <br>
Risk: Generated guidance could introduce incorrect or misleading architecture recommendations for a specific codebase. <br>
Mitigation: Treat outputs as design advice, review proposed changes before execution, and independently validate architecture decisions against project constraints. <br>
Risk: Port interfaces can become leaky or drift from the adapters they represent. <br>
Mitigation: Keep ports domain-centered and use contract tests or automated architecture checks to confirm adapters continue to satisfy their port contracts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-hexagonal) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Code] <br>
**Output Format:** [Markdown guidance with architecture steps, deliverables, risks, and concrete component names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces design advice only; users should independently validate architecture changes before applying them.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
