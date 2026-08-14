## Description:

Detects workplace phone use in images or video, sends the media to a cloud vision API, and returns structured monitoring results, warnings, suggestions, history data, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise administrators and authorized workplace operations teams use this skill to analyze office-area images or video for employee phone-use events, compliance scores, warnings, and improvement suggestions. It also supports cloud history lookup for prior monitoring reports linked to the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Employee surveillance and workplace behavior monitoring can be inappropriate or unlawful without authority, notice, consent, and a legitimate business purpose.

Mitigation: Use only in authorized workplace monitoring programs with required employee notice or consent, documented scope, and review against applicable labor, privacy, and surveillance rules.

Risk: Media and report data are sent to a vendor cloud service and may contain employee images, workplace activity, and behavioral inferences.

Mitigation: Review the vendor's retention, access-control, deletion, and data-processing practices before using real workplace footage; limit uploads to necessary media.

Risk: Automatic identity linkage, history retrieval, and local account/token persistence can expose monitoring history or credentials if the runtime is shared or compromised.

Mitigation: Run in a controlled environment, restrict filesystem and account access, protect persisted tokens, and clear local state when rotating users or decommissioning the skill.

Risk: Automated compliance scores and phone-use detections can be wrong or incomplete if image quality, context, or model behavior is unsuitable.

Mitigation: Treat results as management-support information, review important findings manually, and avoid using this skill as the sole basis for employment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Workplace phone behavior monitoring API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, files]

**Output Format:** [Markdown or JSON report text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include compliance scores, detected phone-use counts and duration, warnings, suggestions, cloud history data, and export links.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
