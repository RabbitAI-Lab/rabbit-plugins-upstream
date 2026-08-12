## Description:

Forklift expert helps agents answer forklift questions across brands, product selection, technical troubleshooting, maintenance, parts, used-equipment evaluation, safety, standards, regulations, and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangpf6698](https://clawhub.ai/user/yangpf6698)

### License/Terms of Use:

CC-BY-NC-4.0 + additional noncommercial terms

## Use Case:

External users and agents use this skill as a Chinese-language forklift reference assistant for selecting equipment, diagnosing common faults, planning maintenance, checking parts guidance, and understanding safety or standards topics. Operational recommendations should be verified against the exact model, OEM manual, local rules, and qualified personnel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maintenance, fault diagnosis, test-drive, and safety guidance may be too general for a specific forklift model or worksite.

Mitigation: Verify recommendations against the exact model, serial number, OEM manual, local safety rules, and qualified technicians or licensed operators before acting.

Risk: Standards, regulations, market data, prices, and model specifications can change or vary by region.

Mitigation: Use the skill's standard-retrieval and web verification workflow for current status, dates, prices, and exact specifications before presenting conclusions.

Risk: High-voltage batteries, controllers, hydraulics, and thermal events can create safety hazards if handled from general text guidance alone.

Mitigation: Escalate hazardous repairs to the manufacturer, authorized service provider, or qualified personnel instead of giving step-by-step field repair instructions.

Risk: The artifact license imposes noncommercial attribution terms that may conflict with some reuse scenarios.

Mitigation: Confirm intended use is permitted and retain required attribution to 杨鹏飞 / 叉车技术老炮, or obtain written authorization before commercial reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangpf6698/skills/forklift)
- [SKILL.md](artifact/SKILL.md)
- [AUTHOR.md](artifact/AUTHOR.md)
- [LICENSE.md](artifact/LICENSE.md)
- [brands.md](artifact/brands.md)
- [selection-guide.md](artifact/selection-guide.md)
- [fault-diagnosis.md](artifact/fault-diagnosis.md)
- [maintenance-plan.md](artifact/maintenance-plan.md)
- [parts-consumables.md](artifact/parts-consumables.md)
- [safety-regulation.md](artifact/safety-regulation.md)
- [standard-retrieval.md](artifact/standard-retrieval.md)
- [standards.md](artifact/standards.md)
- [used-forklift-evaluation.md](artifact/used-forklift-evaluation.md)
- [market-trends.md](artifact/market-trends.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown answers with structured checklists, decision notes, and source reminders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to verify current standards, market data, prices, and exact model specifications before answering.]

## Skill Version(s):

2.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
