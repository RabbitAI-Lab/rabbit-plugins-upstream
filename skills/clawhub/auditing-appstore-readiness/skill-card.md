## Description: <br>
Audit an iOS app repo (Swift/Xcode or React Native/Expo) for App Store compliance and release readiness; output a pass/warn/fail report and publish checklist. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tristanmanchester](https://clawhub.ai/user/tristanmanchester) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and release engineers use this skill to audit native iOS, React Native, or Expo repositories before App Store or TestFlight submission. It produces static compliance findings, remediation guidance, and a publish checklist. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The audit can optionally invoke Xcode builds, archives, dependency installs, Expo prebuild, signing automation, or patch steps that execute project code or create artifacts. <br>
Mitigation: Keep the default read-only audit posture unless the user explicitly approves a mutating step; review each proposed build, install, signing, or patch command before execution. <br>
Risk: Static checks cannot fully verify App Store Connect metadata, Privacy Nutrition Labels, export compliance, rights clearance, regional obligations, or in-app purchase configuration. <br>
Mitigation: Include the manual checklist in the final report and require human review before treating the app as ready to submit. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tristanmanchester/skills/auditing-appstore-readiness) <br>
- [Report Template](references/report-template.md) <br>
- [Manual Checklist](references/manual-checklist.md) <br>
- [Permissions Map](references/permissions-map.md) <br>
- [Expo Checks](references/expo.md) <br>
- [React Native Checks](references/react-native.md) <br>
- [Native iOS Checks](references/native-ios.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report with optional JSON audit file and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports PASS/WARN/FAIL findings with evidence, remediation steps, and a publish checklist.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
