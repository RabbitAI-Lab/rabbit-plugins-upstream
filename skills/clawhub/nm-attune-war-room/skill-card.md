## Description: <br>
Convenes a multi-LLM expert panel to pressure-test hard-to-reverse decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical decision makers use this skill to structure high-stakes architectural or strategic deliberations, compare courses of action, pressure-test assumptions, and produce a decision record with dissent, risks, and reversal planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deliberation records may be retained locally or posted to GitHub Discussions. <br>
Mitigation: Confirm storage and deletion expectations before use, and require explicit approval before publishing decision summaries externally. <br>
Risk: The artifact includes fallback guidance using --dangerously-skip-permissions for a GLM command path. <br>
Mitigation: Remove or disable permission-bypass command guidance before installation and use standard approval controls for external model invocations. <br>
Risk: The workflow can execute repo-local scripts for deferred capture or orchestration. <br>
Mitigation: Review repo-local scripts before execution and avoid automatic script execution in untrusted workspaces. <br>
Risk: GitHub Discussion publishing uses the user's authenticated gh credentials. <br>
Mitigation: Verify the target repository, category, and discussion body before publishing, and skip publishing when credentials or repository permissions are not appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-war-room) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>
- [Farnam Street: Reversible and Irreversible Decisions](https://fs.blog/reversible-irreversible-decisions/) <br>
- [One-Way and Two-Way Door Decision-Making](https://tapandesai.com/one-way-two-way-doors-decision-making/) <br>
- [Amazon Type 1 vs Type 2 Decisions](https://ashikuzzaman.com/2025/03/03/amazons-type-1-vs-type-2-decisions-a-framework-for-effective-decision-making/) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown decision records with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save local session artifacts and publish summarized decision records to GitHub Discussions when prerequisites are met and publishing is not declined.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
