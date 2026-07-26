## Description: <br>
Generates, previews, applies, and restores custom WorkBuddy interface skins from a short description or reference image by creating theme CSS and injecting it into WorkBuddy's app package. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chugenice](https://clawhub.ai/user/chugenice) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and WorkBuddy users use this skill to generate visual themes, preview them, apply them to WorkBuddy, and restore the original app package when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill modifies WorkBuddy's installed app.asar package, which can affect signatures, updates, or managed-device policy compliance. <br>
Mitigation: Review the exact target path before applying, use it only where app package modification is allowed, keep app.asar.bak, and restore the backup before updating or if behavior is unexpected. <br>
Risk: Applying a skin can close or restart WorkBuddy and may use a scheduled task to complete the restart. <br>
Mitigation: Run it only when active WorkBuddy sessions can be interrupted, and confirm the patched package exists before applying. <br>
Risk: Security evidence classifies the release as suspicious because it alters the installed app package. <br>
Mitigation: Prefer personal machines, avoid managed or policy-controlled systems without approval, and review the generated theme and target package before installation. <br>


## Reference(s): <br>
- [WorkBuddy skin variable reference](references/variable-reference.md) <br>
- [ClawHub skill page](https://clawhub.ai/chugenice/skills/workbuddy-new) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with PowerShell and Node commands, generated CSS, JSON theme files, and preview HTML] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local-first workflow that produces theme assets, preview files, and app.asar backup, patch, apply, and restore steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence and manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
