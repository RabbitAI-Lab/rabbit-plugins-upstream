## Description: <br>
Summarizes recent git changes for context recovery after session breaks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to get back up to speed on recent repository, document, meeting, sprint, or log changes after a gap or handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation on status, progress, or summary requests may cause the agent to inspect more local repository, document, or log content than intended. <br>
Mitigation: Confirm the intended scope, baseline, and target before running catchup analysis, especially in private or large workspaces. <br>
Risk: Catchup summaries can omit important detail or overstate the significance of recent changes. <br>
Mitigation: Use the summary as a navigation aid and verify important conclusions against referenced files, commits, documents, or logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-catchup) <br>
- [clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summary with bullets, checkboxes, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Summaries are structured around context, delta, insights, follow-ups, and blockers.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
