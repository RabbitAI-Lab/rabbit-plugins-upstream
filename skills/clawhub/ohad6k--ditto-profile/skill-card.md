## Description: <br>
Load the user's Emulo profile, mined from local AI coding session logs, so an agent can work from the user's preferences before starting a task. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ohad6k](https://clawhub.ai/user/ohad6k) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use Emulo to load a locally generated working profile before coding, writing, design, or other personalized tasks. The skill helps an agent apply the user's stated preferences, voice, taste, and known failure modes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to load guidance mined from prior local AI session logs, which may influence future work broadly. <br>
Mitigation: Review the generated profile before allowing agents to use it broadly, and use it only for tasks where personalization is clearly wanted. <br>
Risk: A persistent profile can contain outdated or overly broad preferences if it is reused without review. <br>
Mitigation: Keep the profile scoped to the relevant domain and refresh or edit it when the user's preferences or project context change. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ohad6k/skills/ditto-profile) <br>
- [Emulo Homepage](https://github.com/ohad6k/emulo) <br>
- [Emulo Rename Release](https://github.com/ohad6k/emulo/releases/tag/v0.5.0) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May load a persistent local profile generated from prior AI session logs.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
