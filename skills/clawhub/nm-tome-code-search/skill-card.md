## Description: <br>
Searches GitHub for existing implementations, libraries, or patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to find public GitHub implementations, libraries, and prior art for a topic during research or coding work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic triggers may cause the skill to activate during ordinary coding or search requests. <br>
Mitigation: Review when the skill is invoked and confirm that GitHub public-code search is appropriate for the task. <br>
Risk: The skill is not intended for private local codebase searches. <br>
Mitigation: Use local repository search tools for private codebases instead of invoking this GitHub search skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-tome-code-search) <br>
- [claude-night-market tome](https://github.com/athola/claude-night-market/tree/master/plugins/tome) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Markdown guidance describing search queries, GitHub findings, and ranked implementation references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces public-code search guidance and findings; it is not intended for private local codebase search.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
