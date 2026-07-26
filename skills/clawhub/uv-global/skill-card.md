## Description: <br>
Provision and reuse a global uv environment for ad hoc Python scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guoqiao](https://clawhub.ai/user/guoqiao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and coding agents use this skill when quick Python scripts need additional packages and a project-specific virtual environment would be unnecessary. It provisions a shared uv environment and provides commands for adding packages and running ad hoc scripts from that environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A persistent shared Python environment can accumulate packages and affect future ad hoc scripts in ways that are hard to audit. <br>
Mitigation: Periodically inspect or reset ~/.uv-global, and switch to a project-local virtual environment when a task grows beyond quick scripting. <br>
Risk: Installing uv and preloading packages requires trust in the installer and package supply chain. <br>
Mitigation: Install uv yourself first when possible, review install.sh before running it, and only prepend ~/.uv-global/.venv/bin to PATH when that behavior is needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/guoqiao/skills/uv-global) <br>
- [Metadata Homepage](https://github.com/guoqiao/skills/blob/main/uv-global/uv-global/SKILL.md) <br>
- [uv Installer](https://astral.sh/uv/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may recommend installing packages into a persistent ~/.uv-global environment and optionally adding ~/.uv-global/.venv/bin to PATH.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
