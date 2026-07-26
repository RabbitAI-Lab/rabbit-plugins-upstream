## Description: <br>
Bash tool that generates a Supervisor (supervisord) `[program:*]` config file from zero CLI flags by deriving the program name, command path, working directory, user, log paths, and output filename from the current app directory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to generate a basic Supervisor program config for an app directory that already contains a `run.sh` entrypoint. It is suited for quick single-app Supervisor setup when the default generated settings are acceptable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill silently overwrites `<dirname>-supervisor.conf` in the current directory. <br>
Mitigation: Check for an existing generated config and preserve any manual edits before running the tool. <br>
Risk: The generated Supervisor config controls what Supervisor runs and which user it runs as. <br>
Mitigation: Review the generated config before moving or linking it into Supervisor's active configuration path. <br>
Risk: The generated `command` references `run.sh` without validating that the file exists or is safe to execute. <br>
Mitigation: Confirm the target app directory contains the intended `run.sh` entrypoint before enabling the config. <br>


## Reference(s): <br>
- [supervisor-config-gen setup + full reference](artifact/references/setup.md) <br>
- [supervisor-config-gen ClawHub page](https://clawhub.ai/psyb0t/skills/supervisor-config-gen) <br>
- [supervisor-config-gen GitHub repository](https://github.com/psyb0t/supervisor-config-gen) <br>


## Skill Output: <br>
**Output Type(s):** [configuration, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated Supervisor INI configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates a local `<dirname>-supervisor.conf` file in the current directory and may overwrite an existing file with that name.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
