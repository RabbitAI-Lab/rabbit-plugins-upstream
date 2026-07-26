## Description: <br>
Drives the installed FinalPlace Windows desktop app's auto-rules engine to organize files by translating explicit FinalPlace requests into confirmed sorting, moving, copying, compressing, unzipping, or renaming workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[csjfeiyang-arch](https://clawhub.ai/user/csjfeiyang-arch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and Windows users with FinalPlace installed use this skill to turn explicit FinalPlace file cleanup, archiving, and batch-processing requests into CLI-driven rules with preview, confirmation, execution, reporting, and cleanup steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can invoke a powerful file-moving and deleting rules engine for file cleanup requests. <br>
Mitigation: Before any run, verify the source folder, match conditions, action, destination, persistence or schedule settings, and prefer a dry run or preview before move, delete, rename, unzip, compress, or all-files execution. <br>
Risk: Overbroad FinalPlace rule execution can modify many files if the requested scope is wrong. <br>
Mitigation: Require explicit user confirmation for file-modifying actions and report execution statistics so the user can verify matched, successful, failed, and skipped counts. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/csjfeiyang-arch/finalplace-auto-organize) <br>
- [ClawHub skill listing](https://clawhub.ai/csjfeiyang-arch/skills/finalplace-auto-organize) <br>
- [FinalPlace product site](https://www.finalplace.cn/) <br>
- [FinalPlace English product site](https://www.finalplace.cn/en/) <br>
- [FinalPlace Windows installer](https://d.finalplace.cn/windows/FinalPlace_Setup.exe) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline command examples and JSON condition snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the installed FinalPlace Windows application and the FINALPLACE_EXE environment variable or FinalPlace executable discovery.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
