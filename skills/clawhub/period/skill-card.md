## Description: <br>
Tracks menstrual cycles, logs symptoms, and predicts periods, ovulation, and fertile windows from the user's own logged data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to keep a local menstrual-cycle and symptom log, estimate upcoming periods and fertility windows, and identify patterns or red flags that should be discussed with a clinician. It advises and organizes personal records; it does not diagnose conditions or replace clinical care. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates and reads local files containing sensitive menstrual and symptom history. <br>
Mitigation: Review the configured local storage path before use, avoid syncing the directory, and use the export or deletion workflow when records should no longer be kept. <br>
Risk: Cycle predictions and symptom guidance can be wrong or insufficient for urgent health concerns. <br>
Mitigation: Treat outputs as tracking support, keep red-flag guidance clinician-first, and do not use the skill as a diagnosis or emergency-care substitute. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/period) <br>
- [Clawic Period Tracker](https://clawic.com/skills/period) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Conversational text plus local Markdown and YAML records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores cycle, symptom, configuration, and memory records locally under the configured period-tracking directory.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
