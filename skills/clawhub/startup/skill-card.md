## Description: <br>
Orchestrates startup work by routing founder questions to specialized agents and applying stage-appropriate priorities for product-market fit, growth, hiring, fundraising, runway, and burn decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Founders and startup operators use this skill to prioritize decisions, synthesize cross-functional agent input, and frame advice around stage, runway, business model, and risk posture. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may record startup context such as stage, business model, runway, and preferences under ~/Clawic/data/startup/. <br>
Mitigation: Review what context is stored there and avoid saving confidential founder, customer, financial, or legal details unless they are needed for future advice. <br>
Risk: Founder guidance can be misleading if stage, runway, or business model assumptions are wrong or stale. <br>
Mitigation: Confirm the current stage, runway, business model, and risk posture before relying on strategic recommendations. <br>
Risk: Multi-agent routing can synthesize advice across product, growth, finance, legal, hiring, and sales decisions that affect real business outcomes. <br>
Mitigation: Use the output as decision support and have the founder or responsible specialist review material financial, legal, hiring, or fundraising actions before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/startup) <br>
- [Clawic Startup skill homepage](https://clawic.com/skills/startup) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration] <br>
**Output Format:** [Markdown or text guidance with optional local configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use founder-provided startup context such as stage, business model, runway, and preferences to tailor recommendations.] <br>

## Skill Version(s): <br>
1.0.3 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
