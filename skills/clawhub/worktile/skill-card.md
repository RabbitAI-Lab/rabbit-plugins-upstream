## Description: <br>
Extract and summarize public project and announcement information from Worktile shared pages without requiring login or accessing private data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[CodeKungfu](https://clawhub.ai/user/CodeKungfu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and internal teams use this skill to summarize public Worktile announcement and project pages, including titles, authors, update times, task groups, status distributions, and resource links. It is intended for public shared pages only, not private team content or account operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be applied to private or restricted Worktile content even though it is intended only for public shared pages. <br>
Mitigation: Use it only on Worktile pages the user is allowed to view and share; do not process private team content unless it has been intentionally made public and is appropriate for internal analysis. <br>
Risk: Repeated parsing of dynamically loaded pages could create unnecessary duplicate access. <br>
Mitigation: Wait for page rendering to complete and apply frequency controls to avoid repeated visits. <br>


## Reference(s): <br>
- [ClawHub Worktile release](https://clawhub.ai/CodeKungfu/worktile) <br>
- [Worktile homepage](https://worktile.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown summaries and structured lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No account login, private data access, code execution, or persistence requested.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
