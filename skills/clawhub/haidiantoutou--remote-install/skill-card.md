## Description: <br>
Automates Windows software installation by detecting installer packages and using silent commands or GUI automation for software such as Office, Adobe, Chrome, and archive tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, IT operators, and support staff use this skill to find and install Windows software packages on local or RustDesk-connected machines, with configurable installer search paths, UI button labels, timeouts, and software-type matching. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute discovered Windows installers and drive installation dialogs. <br>
Mitigation: Use exact trusted installer paths, review detected packages, avoid bulk install requests, and require explicit confirmation before each package is installed. <br>
Risk: Remote-access credentials and package paths may be logged during RustDesk workflows. <br>
Mitigation: Remove or redact password logging and avoid storing sensitive remote IDs, credentials, or package paths in retained logs. <br>
Risk: Shell-based installer execution can run unexpected installer behavior. <br>
Mitigation: Prefer vetted MSI or EXE packages, avoid shell-based execution where possible, and run installations in a controlled Windows session with appropriate privileges. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haidiantoutou/skills/remote-install) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON result summaries with supporting shell command and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes success and failure counts, package paths, detected software type, recommended architecture, and verification status when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
