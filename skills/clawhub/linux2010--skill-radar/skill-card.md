## Description: <br>
Skill Radar helps an agent find relevant skills by searching installed skills, skills.sh, and GitHub, then ranking results with quality and risk cues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linux2010](https://clawhub.ai/user/linux2010) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to discover, compare, and install agent skills for a task when no suitable local skill is obvious. It is intended to produce ranked recommendations and installation guidance rather than execute the recommended skills automatically. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can proactively search external sources and recommend third-party skills that may alter future agent behavior. <br>
Mitigation: Review each recommended skill's source, publisher, permissions, and installation scope before approving installation. <br>
Risk: Global installation guidance can affect later agent sessions beyond the immediate task. <br>
Mitigation: Install only after explicit user confirmation and prefer the narrowest practical installation scope when available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linux2010/skills/skill-radar) <br>
- [Search tips and category reference](references/search-tips.md) <br>
- [skills.sh](https://skills.sh/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with tables and inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Recommendations may include quality labels, risk markers, and install commands for user-approved skills.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
