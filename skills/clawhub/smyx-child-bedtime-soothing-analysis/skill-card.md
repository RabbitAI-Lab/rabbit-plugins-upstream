## Description:

Analyzes child bedroom nighttime audio and video to detect pre-sleep crying, fear-of-dark behaviors, nightmare awakenings, and related unrest, then returns structured soothing actions such as night-light, recorded-story, lullaby, or parent-notification recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators can use this skill to analyze authorized child-bedroom sleep-window media and produce structured reports for bedtime unrest, nightmare wakeups, and escalation-oriented soothing workflows. It is intended for behavioral event detection and caregiver workflow support, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child bedroom audio/video may be sent to a backend service and associated with an automatically managed identity.

Mitigation: Require explicit guardian consent, restrict accepted files and URLs to trusted cameras or storage, and confirm identity, token, report, retention, and deletion controls before deployment.

Risk: Weak user-control boundaries could make it unclear how caregivers pause monitoring or prevent unintended collection.

Mitigation: Expose clear caregiver controls for pausing monitoring, adjusting sleep windows, opting out permanently, and reviewing what reports are retained.

Risk: The artifact operates on child sleep behavior and could be mistaken for medical or psychological assessment.

Mitigation: Present outputs as behavioral event detection and soothing workflow guidance only, and route repeated or severe concerns to qualified pediatric sleep or child mental-health professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis)
- [API reference](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with optional saved text output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include detected event labels, audio/video signals, soothing actions, escalation recommendations, historical report links, and caregiver-facing safety guidance.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
