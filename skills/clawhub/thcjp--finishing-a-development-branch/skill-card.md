## Description: <br>
Guides agents through finishing a development branch by reviewing completed implementation status, passing tests, and integration next steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill when implementation work is complete and they need structured guidance for branch wrap-up, verification, and integration decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives broad and vague automation guidance around commands, credentials, APIs, files, and automatic activation. <br>
Mitigation: Constrain when the skill runs, require confirmation before shell commands or external API calls, and review the exact workflow before installation. <br>
Risk: Use of privileged credentials could expand the impact of unclear branch-finishing actions. <br>
Mitigation: Provide only least-privilege, task-specific credentials and avoid exposing privileged tokens unless the requested workflow is explicit. <br>
Risk: Branch integration guidance can affect source code, configuration, and release state. <br>
Mitigation: Review proposed diffs, commands, and test results before merging or publishing branch changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/finishing-a-development-branch) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-like structured responses with command and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include status, result metadata, error details, troubleshooting guidance, and next-step recommendations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
