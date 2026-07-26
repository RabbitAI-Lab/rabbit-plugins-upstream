## Description: <br>
Catalyst Design provides catalyst composition, structure, synthesis, condition, and validation guidance from a layered, traceable methodology base and optional catalyst-search literature matrices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andypeng09](https://clawhub.ai/user/andypeng09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and research teams use this skill to draft catalyst design proposals for reactions such as HER, OER, ORR, PEMWE, water splitting, photocatalysis, and plastic upcycling. It is most useful when the user provides a reaction goal and material system or a catalyst-search literature matrix. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The opt-in methodology update path can modify the skill's own reference files if the user explicitly asks the agent to update or remember methodology. <br>
Mitigation: Keep the skill read-only during normal use; only trigger updates after an explicit user request and review the changed methodology and registry entries before relying on them. <br>
Risk: Catalyst design recommendations may include empirical or under-evidenced rules that require laboratory validation. <br>
Mitigation: Require source tags, confidence labels, and an actionable validation path; treat empirical entries as pending until upgraded with traceable literature or experimental evidence. <br>


## Reference(s): <br>
- [Catalyst Design Methodology System](references/design_methodology.md) <br>
- [Traceability Registry](references/methodology_registry.md) <br>
- [Methodology Update Protocol](references/methodology_update_protocol.md) <br>
- [Design Proposal Template](templates/design_proposal.md) <br>
- [Project homepage](https://github.com/ANDYPENG09/catalyst-design-skill) <br>
- [ClawHub listing](https://clawhub.ai/andypeng09/skills/catalyst-design-skill) <br>
- [Companion catalyst-search skill](https://github.com/ANDYPENG09/catalyst-search-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown design proposal with source tags, confidence labels, citations, and validation steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include GB/T 7714 citations and methodology IDs when literature or registry evidence is used.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter, changelog, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
