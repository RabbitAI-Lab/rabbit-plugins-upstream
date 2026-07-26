## Description: <br>
Audits a named GitHub repository for duplicate pull requests and missing issue-to-PR links, producing a report before any optional comment posting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glucksberg](https://clawhub.ai/user/glucksberg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and repository maintainers use this skill to find evidence-backed relationships between pull requests and issues at repository scale. It is intended for explicit cross-reference analysis requests and keeps labeling and closing decisions manual. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads repository PR and issue metadata and sends compact indexes to analysis subagents. <br>
Mitigation: Use a read-only GitHub token for analysis and avoid private or sensitive repositories unless the operator accepts that processing. <br>
Risk: Generated cross-reference findings or proposed comments could be wrong or misleading. <br>
Mitigation: Review the report evidence and every comment body before approval; keep ambiguous findings in manual review. <br>
Risk: Optional comment posting can mutate GitHub issues or pull requests. <br>
Mitigation: Require both an approved comment queue and the --execute flag; labels and closes remain manual maintainer actions. <br>


## Reference(s): <br>
- [Cross-Ref Principles](references/principles.md) <br>
- [Comment Approval and GitHub API Safety](references/commenting-strategy.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/glucksberg/skills/cross-ref) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown reports with JSON work files and approval queues] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes dry-run reports first; approved comment posting requires a reviewed approval file and an explicit execution flag.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
