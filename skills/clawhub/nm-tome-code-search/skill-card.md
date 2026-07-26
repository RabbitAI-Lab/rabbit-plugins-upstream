## Description: <br>
Searches GitHub for existing implementations, libraries, or patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and research agents use this skill to find existing GitHub implementations, libraries, examples, and prior art during code research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic triggers such as code and search may activate the skill during unrelated conversations. <br>
Mitigation: Narrow triggers or invocation rules when the host agent supports them, and review whether GitHub search assistance is intended before use. <br>
Risk: Search terms may be sent to WebSearch or GitHub during GitHub implementation research. <br>
Mitigation: Avoid submitting confidential code names, private repository details, secrets, or sensitive proprietary implementation details as search queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-tome-code-search) <br>
- [Tome plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/tome) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code] <br>
**Output Format:** [Markdown guidance with GitHub search findings and implementation references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce ranked Finding objects when used as part of the Tome research workflow.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
