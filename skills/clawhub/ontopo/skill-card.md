## Description: <br>
Find Israeli restaurants, check table availability across dates and venues, view menus, and return Ontopo booking links for manual completion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexpolonsky](https://clawhub.ai/user/alexpolonsky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to discover restaurants in Israel, compare live Ontopo availability, inspect menus, and obtain booking links for manual reservation completion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Restaurant search details are sent to Ontopo for live availability lookup. <br>
Mitigation: Use the skill only when sharing those search details with Ontopo is acceptable. <br>
Risk: Live availability may be incomplete or stale, and the skill does not confirm reservations. <br>
Mitigation: Treat results as leads and complete or confirm reservations manually on Ontopo using the returned booking links. <br>


## Reference(s): <br>
- [Ontopo Hotfix on ClawHub](https://clawhub.ai/alexpolonsky/skills/ontopo) <br>
- [alexpolonsky ClawHub Profile](https://clawhub.ai/user/alexpolonsky) <br>
- [Ontopo Website](https://ontopo.com) <br>
- [Ontopo API Base](https://ontopo.com/api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Human-readable CLI text or JSON envelopes, with Markdown guidance and command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns booking URLs for manual confirmation on Ontopo; does not place reservations.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
