## Description: <br>
HarmonyOS 7 (API 26) coding assistant for ArkTS and ArkUI development, including code generation, migration checks, API guidance, and project release support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fff-119](https://clawhub.ai/user/fff-119) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design, write, review, and troubleshoot HarmonyOS applications with ArkTS, ArkUI, Stage model architecture, Kit references, and release checklists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs the agent to persist conversation-derived lessons into its own expert files and re-register itself. <br>
Mitigation: Install only after removing or disabling automatic learning, file-update, and re-registration behavior, or require explicit human approval for any persistent changes. <br>
Risk: Generated HarmonyOS code or API guidance may be incorrect, stale, or mismatched with the user's DevEco Studio and HarmonyOS API target. <br>
Mitigation: Review generated code and guidance, verify API compatibility against the target HarmonyOS version, and run normal build and test checks before relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fff-119/skills/harmonyos-code-workshop) <br>
- [HarmonyOS UIAbility overview](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/uiability-overview-V5) <br>
- [HarmonyOS UIAbility lifecycle](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/uiability-lifecycle-V5) <br>
- [ArkTS Patterns](https://github.com/OpeNopEn2007/arkts-patterns) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with ArkTS and ArkUI code blocks, checklists, commands, and Chinese explanatory text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include HarmonyOS API version labels, self-check notes, migration warnings, and release checklist items.] <br>

## Skill Version(s): <br>
5.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
