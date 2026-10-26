## Description:

Turn user-provided meeting text into evidence-cited minutes and action items using the current model, validate the structured JSON against exact quotes, then save local Markdown and task CSV.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and meeting facilitators use this skill to turn supplied meeting text into evidence-cited minutes, decisions, action items, and unresolved questions, then review and export local reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential meeting notes and quotations may be retained in local output files, and prompts to the configured model may leave the host.

Mitigation: Use a model approved for confidential notes, confirm data handling before processing, and protect or delete local outputs as appropriate.

Risk: Quote matching does not prove that an extracted responsibility or date is semantically correct.

Mitigation: Review extracted responsibilities and dates against their cited meeting text before relying on the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hznetnewpower/skills/mochi-meeting-actions)
- [MochiLab](https://mochilab.bz/)

## Skill Output:

**Output Type(s):** [Markdown, JSON, CSV]

**Output Format:** [Local meeting report and task-list files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source quotations; unspecified owners and dates remain unknown.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
