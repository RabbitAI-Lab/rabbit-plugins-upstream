## Description: <br>
Before the user starts coding a new project idea, search GitHub for an existing repo to fork as a starting point. Skip for debugging, learning, or a specific algorithm/function. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gdwhisper](https://clawhub.ai/user/gdwhisper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and builders use this skill before starting a new project to search GitHub for reusable starter repositories, compare candidate fit, and decide whether to fork, extend, reference, or build fresh. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using GITHUB_TOKEN can expose broader GitHub access than needed for public repository search. <br>
Mitigation: Use a minimally scoped token, or leave GITHUB_TOKEN unset when unauthenticated public search is enough. <br>
Risk: Repository recommendations can be incomplete or stale because they depend on GitHub search results and repository metadata. <br>
Mitigation: Review candidate repositories before forking, including maintenance activity, license, and fit for the intended project. <br>


## Reference(s): <br>
- [Script Reference](references/schema.md) <br>
- [ClawHub skill page](https://clawhub.ai/gdwhisper/skills/fork-it) <br>
- [GitHub repository search API endpoint](https://api.github.com/search/repositories) <br>
- [GitHub repository details API endpoint](https://api.github.com/repos) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and summarized repository data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use GitHub API results and an optional GITHUB_TOKEN for higher rate limits.] <br>

## Skill Version(s): <br>
3.0.1 (source: release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
