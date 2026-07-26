## Description: <br>
Applies layered n-tier architecture with enforced boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and software architects use this skill to decide when layered or n-tier architecture fits moderate systems and to plan layer responsibilities, dependency rules, ADRs, diagrams, and architecture checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic architecture and domain triggers may activate this guidance in broad design conversations where layered architecture is not the right fit. <br>
Mitigation: Confirm the system context matches the skill's stated layered or n-tier use cases before following recommendations. <br>
Risk: Strict layering can create pass-through code or latency for features that naturally cross layers. <br>
Mitigation: Use the documented facade or exception guidance and review tradeoffs before enforcing strict layer boundaries. <br>
Risk: Layer boundary recommendations may be applied without project-specific validation. <br>
Mitigation: Have developers or architects review proposed ADRs, dependency diagrams, and automated checks before adopting them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-layered) <br>
- [Publisher Profile](https://clawhub.ai/user/athola) <br>
- [Project Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with architecture recommendations, deliverable outlines, and example tooling suggestions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable behavior; outputs are advisory and should be reviewed before applying to architecture decisions.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
