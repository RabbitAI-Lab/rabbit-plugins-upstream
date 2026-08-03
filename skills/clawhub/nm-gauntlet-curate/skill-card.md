## Description: <br>
Adds developer-authored annotations to the gauntlet knowledge base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to capture project-specific rationale, rules, and tribal knowledge as annotations that can be reused by future agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Annotation content may include secrets, credentials, or private internal details that should not be reused. <br>
Mitigation: Review annotation text before saving and remove sensitive or confidential information. <br>
Risk: An unsafe filename slug could create an unexpected local annotation path. <br>
Mitigation: Use a simple, project-appropriate slug before creating the YAML file under .gauntlet/annotations/. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-curate) <br>
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, files] <br>
**Output Format:** [Markdown guidance and local YAML annotation file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates a YAML annotation under .gauntlet/annotations/.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
