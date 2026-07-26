## Description: <br>
酷家乐设计-免费版 guides an agent through a step-by-step interior-design workflow for confirming floor plans, selecting styles, generating layouts, and producing render or panorama links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and personal design learners use this skill to preview home-renovation ideas, search or upload floor plans, select basic hard-decoration styles, and request Kujiale-powered layout and rendering outputs through an agent-guided workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to provide a Kujiale API token and may handle floor plans or related design data. <br>
Mitigation: Treat the API token as sensitive, keep it out of shared projects, shell history, logs, and version control, and use the skill only when sharing design data with Kujiale is acceptable. <br>
Risk: The security summary says the package only contains Markdown instructions and does not provide the runtime scripts referenced by the command examples. <br>
Mitigation: Confirm or supply the required runtime implementation before executing commands, and review any added scripts before use. <br>


## Reference(s): <br>
- [Kujiale Skills](https://www.kujiale.com/skills) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/kujiale-design-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, shell command examples, and structured JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing workflow steps and expected response fields; the release evidence indicates missing runtime scripts must be supplied by the user.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
