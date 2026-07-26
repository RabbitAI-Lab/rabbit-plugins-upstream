## Description: <br>
BlazeMeter Functional (blazemeter.com). Use this skill for ANY BlazeMeter Functional request - searching and reading data. Whenever a task involves BlazeMeter Functional, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query BlazeMeter Functional data through an OOMOL-connected account. It supports reading active sessions, listing multi-tests in a workspace, and fetching a multi-test by collection ID. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill allows an agent to read BlazeMeter Functional data through the user's OOMOL-connected account. <br>
Mitigation: Install only when the user intends to grant this read access, and review OOMOL CLI setup and account connection steps before first use. <br>
Risk: Future connector versions could add write or destructive actions. <br>
Mitigation: Keep write actions subject to exact payload review and require explicit user confirmation for destructive actions. <br>


## Reference(s): <br>
- [BlazeMeter Functional homepage](https://www.blazemeter.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-blaze-meter-functional) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are returned as JSON data with execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
