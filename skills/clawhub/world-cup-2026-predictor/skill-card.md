## Description: <br>
Produces English or Chinese football forecasts, pre-kickoff alerts, post-match reviews, and controlled model-evolution analysis from multi-book odds, market movement, match context, and verified results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youjunzhao](https://clawhub.ai/user/youjunzhao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and analysts use this skill to structure football match forecasts, rolling pre-kickoff checks, and post-match calibration reviews. It supports bilingual English/Chinese analysis while emphasizing evidence quality, market-source provenance, and abstention when inputs are insufficient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper scripts may create local forecasting, review, and evolution records that contain match notes or other user-provided context. <br>
Mitigation: Use --no-record when persistence is not needed, choose a controlled --data-dir for retained records, and avoid entering sensitive internal or proprietary notes unless local storage is acceptable. <br>
Risk: Football forecasts and betting-market analysis can be mistaken for guaranteed outcomes or profit advice. <br>
Mitigation: Treat outputs as analytical guidance, preserve the skill's evidence gates and abstention behavior, and avoid guarantee, certainty, or income claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/youjunzhao/skills/world-cup-2026-predictor) <br>
- [Source Policy](references/source-policy.md) <br>
- [Consensus Model](references/consensus-model.md) <br>
- [Market Rules](references/market-rules.md) <br>
- [Odds Formats](references/odds-formats.md) <br>
- [Post-Match Review And Controlled Evolution](references/postmatch-evolution.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown analysis with optional JSON diagnostics and shell commands for bundled helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Helper scripts may create local JSONL ledgers and profile artifacts unless run with --no-record or a chosen --data-dir.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
