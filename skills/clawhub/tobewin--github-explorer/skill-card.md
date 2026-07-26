## Description: <br>
Discover and analyze top GitHub open-source projects in any domain via natural language, with repository search, README retrieval, and plain-language project analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and technical users use this skill to find relevant GitHub repositories and understand what a repository does, how active it is, and whether it fits their needs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and repository names are sent to GitHub API. <br>
Mitigation: Use this skill only when sending those queries to GitHub is acceptable; avoid sensitive private project names or confidential search terms. <br>
Risk: The skill can use a GitHub token for API access. <br>
Mitigation: Use a least-privilege token, preferably read-only or public-repository scoped, and rotate it according to local credential policy. <br>
Risk: Search and README analysis results can be cached under ~/.cache/github-explorer/. <br>
Mitigation: Use --no-cache for sensitive work or run cache clear when retained results are not desired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tobewin/skills/github-explorer) <br>
- [Publisher Profile](https://clawhub.ai/user/tobewin) <br>
- [GitHub REST API Endpoint](https://api.github.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON returned by the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search and repository analysis output may include GitHub repository metadata, README excerpts, local cache status, and rate-limit guidance.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
