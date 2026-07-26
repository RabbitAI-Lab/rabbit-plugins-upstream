## Description: <br>
Routes Chinese private-domain operations requests to onboarding, copywriting, group messaging, conversation, diagnosis, customer-record workflows, or owner-facing setup guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maojiebc](https://clawhub.ai/user/maojiebc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Chinese-speaking private-domain operators, store owners, and small business users use this skill as a single entry point for deciding the next operational step and getting routed guidance or deliverables. It supports onboarding, pre-task routing, post-task navigation, and a zero-dependency restaurant-owner setup guide. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads the current conversation to choose another skill, so incomplete context or ambiguous requests can route work to the wrong next step. <br>
Mitigation: Use explicit commands or provide the current goal clearly when possible, and review the selected next step before relying on the output. <br>
Risk: Companion skills such as save, restore, report, and update can affect customer-record workflows or update behavior. <br>
Mitigation: Review companion skills before installation or use when customer-record storage, retention, reporting, or update behavior matters. <br>
Risk: Generated operational guidance, marketing copy, SVG, HTML, or shell commands may need business, brand, compliance, or execution review. <br>
Mitigation: Review outputs before publishing content, sharing customer-facing assets, or running commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-siyu-team) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/maojiebc) <br>
- [New user tutorial](references/新手教程.md) <br>
- [Owner-facing private-domain setup guide](references/整盘怎么搭-老板版.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese Markdown guidance with routed task instructions, optional SVG/HTML snippets, and inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes to companion siyu skills when available and can produce bundled zero-dependency owner guidance from reference material.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
