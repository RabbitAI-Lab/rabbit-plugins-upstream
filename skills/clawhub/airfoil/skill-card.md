## Description: <br>
Control AirPlay speakers via Airfoil from the command line. Connect, disconnect, set volume, and manage multi-room audio with simple CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asteinberger](https://clawhub.ai/user/asteinberger) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers on macOS use this skill to ask an agent for Airfoil speaker control commands that list, connect, disconnect, set volume, and check multi-room audio status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Speaker names are interpolated into AppleScript commands, creating a local automation injection risk on macOS. <br>
Mitigation: Use only trusted speaker names, validate names against the skill's list output, and patch the script to pass speaker names as osascript arguments or strictly escape them before use. <br>
Risk: The skill requires macOS Accessibility permission for local automation of Airfoil. <br>
Mitigation: Grant Accessibility access only to a trusted terminal or agent environment and revoke it when the skill is no longer needed. <br>


## Reference(s): <br>
- [Airfoil ClawHub skill page](https://clawhub.ai/asteinberger/skills/airfoil) <br>
- [Airfoil for Mac](https://rogueamoeba.com/airfoil/mac/) <br>
- [ClawHub publisher profile: asteinberger](https://clawhub.ai/user/asteinberger) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and short status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [macOS-only; commands call Airfoil through osascript and require local Accessibility permissions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
