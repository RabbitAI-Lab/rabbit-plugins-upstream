## Description: <br>
Plans, creates, and edits Meta Ads campaigns with documented rationale and operational standards through a connected Meta Ads MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[moskoweb](https://clawhub.ai/user/moskoweb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and agents use this skill to translate Meta Ads briefings into campaign, ad set, ad, creative, naming, tracking, readiness, and launch plans, then build or edit those assets through an authorized Meta Ads MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to mutate Meta Ads accounts, including campaigns, ad sets, ads, creatives, budgets, objectives, and tracking. <br>
Mitigation: Install only for agents that should operate on Meta Ads accounts, verify the selected ad account and campaign details before execution, and keep newly created assets paused until reviewed. <br>
Risk: Incorrect account, budget, objective, tracking, or structural choices could affect live advertising operations. <br>
Mitigation: Use the release guidance to verify account selection, budget, objective, tracking, and approval for structural or budget changes before resuming or publishing campaigns. <br>


## Reference(s): <br>
- [Campaign Build Playbooks](references/campaign-build-playbooks.md) <br>
- [Ad Set Structures](references/adset-structures.md) <br>
- [Creative Assembly](references/creative-assembly.md) <br>
- [Launch Checklist](references/launch-checklist.md) <br>
- [Editing Guidelines](references/editing-guidelines.md) <br>
- [Official Meta Build Guidelines](references/official-meta-build-guidelines.md) <br>
- [Meta Performance Marketing](https://www.facebook.com/business/ads/performance-marketing) <br>
- [Meta Advantage+ Placements](https://www.facebook.com/business/ads/meta-advantage-plus/placements) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured plans, checklists, rationale, and tool-call instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an authorized Meta Ads MCP; asset creation starts paused and major structural or budget changes require approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
