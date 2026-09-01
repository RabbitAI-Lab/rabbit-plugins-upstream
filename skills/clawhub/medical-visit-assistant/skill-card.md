## Description:

A medical visit preparation and health-information organization assistant that helps users collect symptoms, build timelines, summarize medical information, explain examination reports in plain language, prepare clinician questions, organize medications and visit notes, and provide cautious urgency reminders without diagnosing or prescribing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zoewhatever-tech](https://clawhub.ai/user/zoewhatever-tech)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to prepare for medical appointments, organize symptoms and visit records, understand examination report terminology in plain language, and prepare questions for clinicians. It is intended to support communication and information organization, not diagnosis, prescribing, or emergency triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake organized health information or plain-language report explanations for diagnosis or treatment advice.

Mitigation: State that outputs are informational, preserve uncertainty, distinguish clinician-reported conclusions from assistant interpretation, and direct diagnosis or treatment decisions to qualified clinicians.

Risk: Urgent or worsening symptoms may require immediate medical assessment.

Mitigation: Prioritize local emergency or clinical care reminders before routine information collection when severe, sudden, or rapidly worsening symptoms are described.

Risk: The skill may process sensitive medical details supplied by the user.

Mitigation: Ask only for medically relevant missing details, avoid unnecessary personally identifying information, and avoid repeating sensitive information when it is not needed.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Chinese Markdown summaries, explanations, question lists, checklists, and visit records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates user-provided information and clinician-reported conclusions from assistant interpretation, preserves uncertainty, and includes safety reminders when appropriate.]

## Skill Version(s):

1.0.0 (source: server release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
