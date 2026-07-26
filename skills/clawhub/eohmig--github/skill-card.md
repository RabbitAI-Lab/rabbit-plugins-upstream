## Description: <br>
Interact with GitHub using the `gh` CLI for issues, pull requests, CI runs, logs, and advanced repository queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eohmig](https://clawhub.ai/user/eohmig) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to inspect GitHub issues, pull requests, CI workflow runs, logs, and repository data with the GitHub CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GitHub CLI commands can use the user's authenticated GitHub permissions, including access to private repositories or write-capable actions. <br>
Mitigation: Install this skill only when the agent should use the authenticated GitHub CLI context, and approve sensitive reads or write actions deliberately. <br>
Risk: Commands may target the wrong repository when repository context is ambiguous. <br>
Mitigation: Specify `--repo owner/repo` or use direct GitHub URLs when the agent is not operating inside the intended git repository. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose `gh` CLI commands that use the user's authenticated GitHub context.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
