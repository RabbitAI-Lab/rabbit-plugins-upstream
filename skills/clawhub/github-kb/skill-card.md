## Description: <br>
Manage a local GitHub knowledge base and provide GitHub search, repository, issue, pull request, and cloning workflows through the GitHub CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jameschan21](https://clawhub.ai/user/jameschan21) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to search GitHub, inspect repositories, issues, and pull requests, clone repositories into a local knowledge base, and maintain a GITHUB_KB.md catalog. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GitHub credentials can expose private repository access if over-scoped or stored directly in files. <br>
Mitigation: Use a limited GitHub token supplied through environment variables or container secrets, and never hardcode tokens. <br>
Risk: Cloning or cataloging private repositories can store sensitive code and metadata in the local knowledge base. <br>
Mitigation: Confirm the KB path and avoid cloning or cataloging private repositories unless local storage is approved. <br>
Risk: GitHub search and repository results may be incomplete when the GitHub CLI is unavailable or unauthenticated. <br>
Mitigation: Verify GitHub CLI installation and authentication before search workflows, or limit use to the existing local KB. <br>


## Reference(s): <br>
- [GitHub CLI Linux installation guide](https://github.com/cli/cli/blob/trunk/docs/install_linux.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and catalog entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local repository clones and GITHUB_KB.md entries when the user requests KB changes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
