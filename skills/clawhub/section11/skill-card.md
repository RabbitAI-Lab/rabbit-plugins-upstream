## Description: <br>
Evidence-based endurance coaching protocol for analyzing athlete training data, reviewing sessions, generating workout reports, planning workouts, and answering endurance coaching questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crankaddict](https://clawhub.ai/user/crankaddict) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Athletes, coaches, and agent operators use this skill to turn Intervals.icu-derived JSON training data into readiness guidance, workout plans, session reviews, weekly or block reports, and calendar-management recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may fetch mutable remote protocol and template files when local files are unavailable. <br>
Mitigation: Prefer local or vendored copies of the protocol and templates, and avoid mutable GitHub fallbacks where possible. <br>
Risk: The skill reads sensitive athlete training data, including activity, wellness, interval, power, heart-rate, and date information. <br>
Mitigation: Install only in trusted environments, keep data local or in private repositories, and use least-privilege credentials for any connected repository. <br>
Risk: Calendar, threshold, and annotation writes can change user training data when write tooling is enabled. <br>
Mitigation: Keep write operations in preview mode by default and require explicit confirmation before any calendar, threshold, or annotation write. <br>
Risk: Heartbeat automation can run recurring analysis and persistence tasks if configured. <br>
Mitigation: Keep heartbeat behavior opt-in and verify the configured notification window, data sources, and destination files before enabling automation. <br>


## Reference(s): <br>
- [Section 11 GitHub repository](https://github.com/CrankAddict/section-11) <br>
- [Data mirror setup](https://github.com/CrankAddict/section-11#2-set-up-your-data-mirror-optional-but-recommended) <br>
- [Section 11 protocol](https://raw.githubusercontent.com/CrankAddict/section-11/main/SECTION_11.md) <br>
- [Dossier template](https://raw.githubusercontent.com/CrankAddict/section-11/main/DOSSIER_TEMPLATE.md) <br>
- [Heartbeat template](HEARTBEAT_TEMPLATE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown guidance with optional shell commands, configuration steps, workout plans, reports, and calendar write previews] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should cite training metrics only after reading the athlete's JSON data in the current response.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release metadata; protocol version 11.35 in SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
