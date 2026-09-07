## Description:

Appium Android Adb helps agents read and control connected Android apps through an OCR-first uiautomator2 workflow with an Appium fallback for native app screens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlittlebear](https://clawhub.ai/user/openlittlebear)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when they need an agent to inspect and act on a connected Android device for explicit app automation tasks. It is best suited to OCR-guided interaction with consumer apps and native-screen fallback through Appium.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control a connected Android device and may trigger live app actions.

Mitigation: Install and use it only for explicit device-control tasks, and require user confirmation before purchases, order submission, account changes, or other irreversible actions.

Risk: Screenshots, OCR output, accessibility trees, and clipboard text can expose sensitive personal or payment-related data.

Mitigation: Treat captured screen data as sensitive, keep payment credentials user-entered only, avoid echoing typed or pasted values, and purge screenshots when no longer needed.

Risk: A persistent Appium bridge daemon can leave device-control capability available longer than intended.

Mitigation: Prefer one-shot commands where possible and stop the Appium bridge daemon after use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/openlittlebear/skills/appium-android-adb)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OCR text, accessibility-tree text, coordinates, and command status from a connected Android device.]

## Skill Version(s):

1.3.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
