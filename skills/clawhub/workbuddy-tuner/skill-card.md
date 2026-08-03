## Description: <br>
WorkBuddy Tuner diagnoses WorkBuddy slowdowns, monitors system and session health, proposes cache, process, and model optimizations, audits sessions, tracks performance trends, and prepares recovery or migration plans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to investigate WorkBuddy performance issues, generate reviewable optimization plans, monitor health trends, and plan backup, migration, or recovery work before changing local state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect local system metrics, process and cache state, device state, and session history. <br>
Mitigation: Install only when this access is expected, and review generated findings before acting on them. <br>
Risk: Cleanup, process management, migration, backup, and scheduled-monitoring workflows can affect local state if executed without review. <br>
Mitigation: Keep these workflows in preview or dry-run mode until explicitly approved, require confirmation for writes or deletions, and verify backups before migration. <br>
Risk: The full skill-matrix install path can introduce additional linked skills beyond this performance tuner. <br>
Mitigation: Review linked skills individually before using the full skill-matrix install option. <br>


## Reference(s): <br>
- [WorkBuddy Tuner on ClawHub](https://clawhub.ai/zxj2devs/skills/workbuddy-tuner) <br>
- [Flow Immersion related skill](https://skillhub.cn/skills/user_11064e10/flow-immersion) <br>
- [WorkBuddy Gift Claimer related skill](https://skillhub.cn/skills/user_11064e10/workbuddy-gift-claimer) <br>
- [Privacymask related skill](https://skillhub.cn/skills/user_11064e10/privacymask) <br>
- [Comprehensive tax knowledge base related skill](https://skillhub.cn/skills/user_11064e10/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and recommendations with optional command snippets, configuration guidance, health scores, alerts, and checklists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include dry-run optimization plans, trend summaries, monitoring thresholds, backup plans, migration checklists, and recovery guidance.] <br>

## Skill Version(s): <br>
3.4.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
