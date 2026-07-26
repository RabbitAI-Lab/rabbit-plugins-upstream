## Description: <br>
Analyze contraction JSON and baby log JSON to assess mum's labour situation and baby's feeding and diaper status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jacklandrin](https://clawhub.ai/user/jacklandrin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and caregivers use this skill to summarize local contraction and baby-care JSON logs, compare them with documented thresholds, and receive scannable monitor or seek-care recommendations with a medical-advice caveat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive health and baby-care logs, and its verdicts could be mistaken for medical advice. <br>
Mitigation: Use the output as a structured summary, include the documented caveat, and contact a midwife, OB, paediatrician, or emergency services for urgent symptoms, uncertainty, or concerning results. <br>
Risk: Incorrect, incomplete, or outdated JSON logs can lead to misleading contraction, feeding, or diaper summaries. <br>
Mitigation: Report the data range, counts, timing statistics, and threshold comparisons so users can verify the source data before acting on the summary. <br>


## Reference(s): <br>
- [Data Schemas and Health/Safety Thresholds](references/schemas-and-thresholds.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with headings and bullet points] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Leads with mum and baby verdicts, includes supporting counts and timing statistics, and ends with a medical-advice caveat.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
