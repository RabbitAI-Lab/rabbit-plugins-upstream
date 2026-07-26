## Description: <br>
Control local CAD applications on Windows including launching apps, opening files, checking status, closing apps, detecting active or running apps, detecting common executable paths, and saving user-provided executable paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhehaiwang](https://clawhub.ai/user/zhehaiwang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and CAD workstation operators use this skill to let an assistant launch supported Windows CAD applications, open CAD files, check running or active applications, and save trusted executable paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Closing CAD applications can disrupt unsaved workstation work, especially when forced close is used. <br>
Mitigation: Confirm work is saved before using close_app, and avoid forced close unless the user explicitly approves it. <br>
Risk: Persisted executable paths could point to the wrong local program. <br>
Mitigation: Only store executable paths that the user personally trusts and recognizes as the intended CAD application. <br>
Risk: The skill gives an assistant control over local Windows CAD applications. <br>
Mitigation: Install and use it only when that local workstation control is intended. <br>


## Reference(s): <br>
- [Artifact README](artifact/README.md) <br>
- [ClawHub skill page](https://clawhub.ai/zhehaiwang/skills/cad-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration] <br>
**Output Format:** [JSON result objects from local Python command execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May launch or close local Windows CAD applications and may update config.json with user-provided executable paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
