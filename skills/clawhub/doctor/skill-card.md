## Description: <br>
Triages symptoms, reads lab results and medication risks, and says how urgent something is: emergency now, seen today, or safe to watch. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill for health triage, lab-result interpretation, medication-safety checks, chronic-condition monitoring, prevention questions, and appointment preparation. It is framed as advice and urgency routing, not diagnosis or prescription management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change sensitive local health records and related personal records. <br>
Mitigation: Install only if a local longitudinal medical record is wanted; review the declared folders and set health_logging to minimal or off if automatic storage is not desired. <br>
Risk: Health guidance could be over-relied on for urgent symptoms, medication decisions, or diagnosis. <br>
Mitigation: Use the output as triage and preparation guidance; follow emergency escalation for red flags and keep prescription-only medication changes with a qualified clinician. <br>
Risk: The security scan found the skill has too little user control over automatic storage. <br>
Mitigation: Review announced writes during use and confirm that updates stay within the declared local Clawic folders before relying on saved records. <br>


## Reference(s): <br>
- [ClawHub Doctor Skill Page](https://clawhub.ai/ivangdavila/skills/doctor) <br>
- [Clawic Doctor Skill Page](https://clawic.com/skills/doctor) <br>
- [Artifact Skill Definition](artifact/SKILL.md) <br>
- [Doctor Working File Templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown and plain-language text with optional local Markdown/YAML note updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces urgency windows, tripwires, clinician-facing questions, prep sheets, and local health-record updates when logging is enabled.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
