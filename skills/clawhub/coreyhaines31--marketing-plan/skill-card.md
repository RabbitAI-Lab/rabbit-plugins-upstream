## Description: <br>
Generates a comprehensive AARRR-structured marketing plan tailored to a client's budget, team, stage, current funnel state, and execution capacity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Founders, marketing teams, fractional CMOs, and marketing consultants use this skill to turn client context, current-state audits, funding stage, budget, team capacity, and funnel goals into a 12-month marketing roadmap. It is intended for comprehensive planning rather than single-channel tactical execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read sensitive client materials while preparing the plan. <br>
Mitigation: Limit the client materials folder to approved documents before invoking the skill. <br>
Risk: The skill may query connected analytics, billing, marketing, or source-control tools for the selected client. <br>
Mitigation: Disable or withhold connectors that should not be queried for the engagement. <br>
Risk: The skill can store derived strategy files under the user's marketing-plans workspace. <br>
Mitigation: Review generated research, progress, section, and final plan files before sharing or retaining them. <br>
Risk: Optional publication to a shared GitHub repository could expose client strategy. <br>
Mitigation: Require explicit user approval and a content review before any publication step. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/coreyhaines31/skills/marketing-plan) <br>
- [Methodology - How a Marketing Plan Gets Made](references/methodology.md) <br>
- [Plan Template - The 13-Section Structure](references/plan-template.md) <br>
- [AARRR Framework - Primer for Plan Sequencing](references/aarrr-framework.md) <br>
- [Current State Rubric - 17-Section Scoring Lens](references/current-state-rubric.md) <br>
- [Budget Planning - Scientific Methods for Setting the Marketing Budget](references/budget-planning.md) <br>
- [Funding-Stage Capability Unlocks](references/funding-stage-unlocks.md) <br>
- [Growth Patterns - The Real Shape of SaaS Growth](references/growth-patterns.md) <br>
- [Idea Cross-Reference - 139 Marketing Ideas Mapped to AARRR](references/idea-cross-reference.md) <br>
- [Marketing Operations Stack - Skills and MCPs per AARRR Stage](references/ops-stack-mapping.md) <br>
- [Measurement Framework - KPIs, North Stars, Cadence](references/measurement-framework.md) <br>
- [Team and Agency Model - Hire for Strategy, Outsource Execution](references/team-and-agency-model.md) <br>
- [Client Types - Variations by Business Model](references/client-types.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Files] <br>
**Output Format:** [Notion-paste-ready Markdown, with supporting planning files when the workflow is run] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a comprehensive 13-section plan and may maintain research, progress, section, and final plan files under the user's marketing-plans workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
