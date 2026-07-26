## Description: <br>
Search skills.sh registry from CLI. Find and discover agent skills from the skills.sh ecosystem. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to search the skills.sh registry, view popular skills, and get install commands for discovered skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Displayed install commands may lead users to add third-party skills with new agent behavior. <br>
Mitigation: Review the target skill, publisher, source repository, and install scope before running any displayed install command. <br>
Risk: Search results depend on the live skills.sh registry response. <br>
Mitigation: Review returned skill details before acting on them and retry later if registry access fails. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thesethrose/skills/skills-search) <br>
- [skills.sh](https://skills.sh) <br>
- [skills.sh API](https://skills.sh/api/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Terminal text output with optional install commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and network access to the skills.sh API.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
