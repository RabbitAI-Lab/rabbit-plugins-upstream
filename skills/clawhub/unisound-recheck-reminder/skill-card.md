## Description: <br>
Generates health exam recheck reminders by extracting abnormal findings from a report, ranking follow-up urgency, and producing structured JSON plus a patient-facing reminder. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Health management teams and exam centers use this skill to turn health exam report text into a ranked recheck checklist with suggested timing, exams, departments, preparation notes, and a recipient-facing reminder. Users should review outputs clinically before sending or relying on them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send health exam reports containing names, IDs, phone numbers, dates, or other health information to a remote LLM endpoint. <br>
Mitigation: Use only reports that have already been de-identified and confirm the LLM endpoint and app key provider are approved for medical data. <br>
Risk: The artifact claims strict de-identification, but the security evidence says the code does not enforce that claim. <br>
Mitigation: Do not rely on the stated de-identification claim unless the code is changed to perform de-identification before the remote request. <br>
Risk: Generated recheck timing and department recommendations could be incomplete or inappropriate for an individual patient. <br>
Mitigation: Have qualified clinical staff review the generated checklist and reminder before use, especially for urgent or high-risk findings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-recheck-reminder) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON followed by a plain-text recheck reminder] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can print to stdout or write the generated reminder to a file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
