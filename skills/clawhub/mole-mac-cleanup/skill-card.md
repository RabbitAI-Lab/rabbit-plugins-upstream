## Description: <br>
Mac cleanup & optimization tool combining CleanMyMac, AppCleaner, DaisyDisk features. Deep cleaning, smart uninstaller, disk insights, and project artifact purge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bjesuiter](https://clawhub.ai/user/bjesuiter) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Mac users use this skill to preview and run Mole cleanup, optimization, uninstaller, disk-insight, and project artifact purge commands on macOS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cleanup, optimization, purge, and installer removal commands can delete local files or change system behavior. <br>
Mitigation: Use the documented dry-run or debug preview commands first and review the planned changes before executing cleanup actions. <br>
Risk: The skill depends on the external Homebrew `mole` package. <br>
Mitigation: Install only when the Homebrew package and its source are trusted. <br>
Risk: `mo touchid`, `mo purge`, `mo installer`, and `mo optimize` can have explicit system or file-removal effects. <br>
Mitigation: Run those commands only when the requested system or cleanup effect is intended. <br>


## Reference(s): <br>
- [Mole Mac Cleanup on ClawHub](https://clawhub.ai/bjesuiter/skills/mole-mac-cleanup) <br>
- [Mole GitHub repository](https://github.com/tw93/Mole) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS with the `mo` command installed from the Homebrew `mole` formula.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
