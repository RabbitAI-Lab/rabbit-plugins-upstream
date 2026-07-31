## Description: <br>
Helps decide whether to reduce price, change the offer, exchange concessions, preserve negotiation room, or hold price when a customer pushes back or gives a target price. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, sourcing, and quotation teams use this skill to structure price negotiation analysis from known quote, cost, customer target, floor price, and concession inputs. It helps identify negotiation stage, adjustable terms, non-negotiable boundaries, recommended strategy, a customer-sendable response, and stop conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive pricing, cost, margin, supplier, and negotiation-boundary information. <br>
Mitigation: Use only appropriately redacted or authorized business data when prompting the skill. <br>
Risk: Negotiation guidance could be mistaken for final approval to commit price, inventory, delivery, compatibility, or customer acceptance terms. <br>
Mitigation: Keep human review and company approval boundaries in place before making final commercial commitments. <br>
Risk: Incomplete or conflicting inputs can lead to premature negotiation recommendations. <br>
Mitigation: Require the parameter status table and use preliminary-analysis mode until required inputs and conflicts are resolved. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zaynpeng/skills/zayn-negotiate) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [examples.md](artifact/examples.md) <br>
- [tests.md](artifact/tests.md) <br>
- [changelog.md](artifact/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, Text] <br>
**Output Format:** [Markdown text with structured negotiation analysis and a customer-facing response draft] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes parameter completeness, parameter status table, negotiation stage, customer request judgment, adjustable items, non-negotiable boundaries, recommended strategy, sendable response, and stop conditions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
