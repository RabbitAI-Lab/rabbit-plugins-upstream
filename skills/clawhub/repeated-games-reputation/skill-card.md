## Description: <br>
Helps agents analyze repeated-game and reputation-system situations by checking whether cooperation is sustainable, selecting an environment-appropriate strategy, and designing reputation infrastructure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to reason about trust, retaliation, cooperation, and reputation-system design in repeated or publicly observed relationships. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill produces strategic analysis that could be mistaken for automatic authority in business, legal, financial, or relationship decisions. <br>
Mitigation: Treat outputs as advisory guidance and require human review before acting on consequential recommendations. <br>
Risk: Repeated-game recommendations can be misleading if the discount factor, observability, noise, or endgame conditions are estimated incorrectly. <br>
Mitigation: Use the skill's verification checklist to confirm repetition structure, discount-factor threshold, observation quality, forgiveness design, and endgame mitigations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deciqai/skills/repeated-games-reputation) <br>
- [Primary Sources](references/sources.md) <br>
- [Robert Axelrod's Computer Tournament Example](examples/robert-axelrod-computer-tournament-1979-1981.md) <br>
- [Trust Reputation as Strategy in the AI Race Example](examples/ai-trust-reputation-enterprise-adoption-2024-2026.md) <br>
- [Agents Metadata](https://www.deciqai.com/s/repeated-games-reputation.json) <br>
- [Axelrod and Hamilton, The Evolution of Cooperation](https://doi.org/10.1126/science.7466396) <br>
- [Fudenberg and Maskin, Folk Theorem](https://doi.org/10.2307/1911307) <br>
- [EU AI Act Official Text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown repeated-game analysis with structured fields and concise recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask one-step clarification questions before analysis in coach mode.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
