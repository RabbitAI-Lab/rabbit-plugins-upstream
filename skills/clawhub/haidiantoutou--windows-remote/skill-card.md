## Description: <br>
Controls remote Windows machines over SSH for command execution, GPU checks, script runs, and file transfers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to administer an explicitly configured Windows host over SSH, including running PowerShell or Python commands, checking NVIDIA GPU status, and moving files with SCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute broad remote commands and transfer files on the configured Windows host. <br>
Mitigation: Use least-privilege SSH credentials, narrow when the skill may be invoked, and require explicit confirmation before uploads, downloads, service changes, or non-read-only commands. <br>
Risk: The bundled SSH and SCP helpers disable strict host key checking. <br>
Mitigation: Verify and pin the Windows host key before use instead of accepting unverified SSH hosts. <br>
Risk: A misconfigured or overprivileged Windows SSH account increases the impact of unintended agent actions. <br>
Mitigation: Limit the account to the intended host and tasks, protect private keys, and prefer network controls such as a private VPN or allowlisted access path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haidiantoutou/skills/windows-remote) <br>
- [Skill source: SKILL.md](artifact/SKILL.md) <br>
- [Release metadata](artifact/_meta.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the ssh binary plus WINDOWS_SSH_HOST and WINDOWS_SSH_USER environment variables; optional settings include WINDOWS_SSH_PORT, WINDOWS_SSH_KEY, and WINDOWS_SSH_TIMEOUT.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
