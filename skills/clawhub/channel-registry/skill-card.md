## Description: <br>
Maintains authoritative records for brand-owned social channels, voice adaptation, cadence, governance, UGC permissions, and advocate facts through an append-only channel registry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators, brand governance teams, and agent workflows use this skill to record or query channel state, cadence, governance, voice pointers, UGC permission, advocate opt-in, and pending social activity or incident proposals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Untrusted channel exports or messages could be mistaken for authoritative channel, governance, or rights records. <br>
Mitigation: Treat exports and messages as evidence only; require explicit source, date, permission, and current revision before saving accepted registry facts. <br>
Risk: UGC permission or advocate records may capture more person or rights data than needed. <br>
Mitigation: Minimize person data and record scope, channels, duration, compensation, expiry, and supporting evidence only when needed. <br>
Risk: Standalone installs may not have the verified runtime needed to append events or project canonical state. <br>
Mitigation: Use standalone installs to prepare proposals only, and claim canonical channel state only after verifying the root runtime, schemas, and catalog. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/channel-registry) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured registry actions and handoff summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce proposed channel, permission, advocacy, cadence, and governance records; standalone installs can prepare proposals but cannot assert canonical state without the verified runtime.] <br>

## Skill Version(s): <br>
19.0.0 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
