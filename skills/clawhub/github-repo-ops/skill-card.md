## Description: <br>
GitHub repository operations and analysis for analyzing code, checking issues, reviewing PRs, tracking stars and releases, searching repositories, and understanding repository structure using public GitHub API data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[blalf](https://clawhub.ai/user/blalf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect public GitHub repositories, compare project health, triage issues, and search for repositories or code relevant to their work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for many GitHub-related prompts and only supports public, read-only repository analysis. <br>
Mitigation: Use it for public repositories only, avoid private or write-operation workflows, and treat its repository health summaries as guidance rather than a definitive security audit. <br>
Risk: Unauthenticated public GitHub API usage is rate limited and code search is limited to public repositories. <br>
Mitigation: Plan analyses around public API limits and verify important findings directly in GitHub before making project or security decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/blalf/skills/github-repo-ops) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown summaries and analysis templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only public GitHub repository analysis; no credentials or private repository access requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
