## Description: <br>
An example ClawHub skill that demonstrates declaring environment variables, dependencies, installation steps, and default configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[feifeifeichangmeilidejutu12138](https://clawhub.ai/user/feifeifeichangmeilidejutu12138) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill as a ClawHub specification example for declaring required credentials, command-line dependencies, supported operating systems, install commands, and simple configuration defaults. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Linux setup command installs curl and jq system-wide with sudo. <br>
Mitigation: Review install commands before running them and allow the sudo apt-get step only in environments where system-wide package installation is acceptable. <br>
Risk: The skill declares API_KEY as a required credential. <br>
Mitigation: Use a scoped test credential and do not provide a real API key unless the target API and runtime environment are trusted. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/feifeifeichangmeilidejutu12138/skills/find-2skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with YAML metadata and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Declares API_KEY as required, BASE_URL and TIMEOUT as optional, and curl, jq, and Python as dependencies for Linux and macOS.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
