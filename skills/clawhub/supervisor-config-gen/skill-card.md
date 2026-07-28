## Description: <br>
Generates a Supervisor program configuration for the current app directory, deriving the program name, command, working directory, user, log paths, and output filename from local shell state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to create a baseline Supervisor program config for an app directory that has a run.sh entrypoint. The generated config should be reviewed before being placed in Supervisor's active include path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated Supervisor config controls what process Supervisor runs and which user runs it. <br>
Mitigation: Review the generated config before enabling it in Supervisor. <br>
Risk: The tool can silently overwrite <dirname>-supervisor.conf in the current directory. <br>
Mitigation: Avoid running it where that file contains manual edits, or back up the file first. <br>
Risk: The generated command points to run.sh without sandboxing or validating that entrypoint. <br>
Mitigation: Verify run.sh before placing the config into Supervisor's active include path. <br>
Risk: Installing or running an unreviewed downloaded script can introduce local execution risk. <br>
Mitigation: Install only from a trusted source and review the downloaded script before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/supervisor-config-gen) <br>
- [Publisher profile](https://clawhub.ai/user/psyb0t) <br>
- [setup.md](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/supervisor-config-gen) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated artifact is an INI-style Supervisor config file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes <dirname>-supervisor.conf in the current directory and may overwrite an existing file with that name.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
