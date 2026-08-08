## Description: <br>
Generates a Supervisor program configuration for the current application directory by deriving the program name, command, working directory, user, and log paths from local shell state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they want an agent to generate or explain a basic supervisord program config for an app directory that contains a run.sh entrypoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation guidance downloads the script from the GitHub master branch, which can change over time. <br>
Mitigation: Review the downloaded script before installation or pin installation to a trusted commit. <br>
Risk: The generated Supervisor config can run an unexpected run.sh, user, or path if the current directory is not the intended target. <br>
Mitigation: Check run.sh, the selected user, the working directory, and log paths before enabling the config in supervisord. <br>
Risk: Re-running the generator silently overwrites <dirname>-supervisor.conf in the current directory. <br>
Mitigation: Back up or review any existing config file before regenerating it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/supervisor-config-gen) <br>
- [Setup and full reference](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/supervisor-config-gen) <br>


## Skill Output: <br>
**Output Type(s):** [configuration, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and Supervisor INI configuration content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces or describes a local <dirname>-supervisor.conf file for a single current working directory.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
