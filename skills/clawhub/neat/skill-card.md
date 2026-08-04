## Description: <br>
End-of-session knowledge cleanup that reconciles project docs, agent guidance files, and cross-session agent memory against the code so knowledge stays current. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill at the end of a development session or milestone to reconcile README, docs, CLAUDE.md/AGENTS.md, and agent memory with the current code state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delete or rewrite project documentation and agent memory. <br>
Mitigation: Review the preview before deletion or batch rewrite, keep work in a git repository when possible, and rely on the skill's documented destructive-operation controls. <br>
Risk: Agent memory or global guidance files may contain private cross-project notes. <br>
Mitigation: Install and run the skill only when those files are intended to be reconciled, and review any proposed memory or global guidance changes before applying them. <br>
Risk: Documentation or memory updates can preserve stale or misleading project guidance if verification is skipped. <br>
Mitigation: Run the documented kb_audit check and re-run verification anchors for status facts before marking synchronization complete. <br>


## Reference(s): <br>
- [Sync Matrix](references/sync-matrix.md) <br>
- [Agent Paths](references/agent-paths.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/vincentjiang06/skills/neat) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and proposed or applied documentation and memory file edits] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update project documentation and agent memory after preview and verification.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence and CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
