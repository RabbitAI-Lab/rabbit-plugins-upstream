## Description: <br>
Create a local Git bundle backup of the OpenClaw workspace repository and report the generated bundle path and size. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[trumppo](https://clawhub.ai/user/trumppo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to create a local backup of the workspace Git repository when they need a restorable bundle of Git history and refs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Git bundles may contain full repository history and any committed secrets. <br>
Mitigation: Protect the backup directory, treat each bundle like a full repository copy, and delete old bundles when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/trumppo/skills/gitbackup) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files] <br>
**Output Format:** [Plain text status output and a local Git bundle file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundle filename includes a UTC timestamp and older bundles are not deleted automatically.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
