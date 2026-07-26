## Description: <br>
Assists community public health staff with chronic disease screening by evaluating resident health data for risks such as hypertension, diabetes, cardiovascular and cerebrovascular disease, COPD, and chronic kidney disease, then returning risk levels and management suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External public health and clinic staff use this skill to screen resident health records for chronic disease risk, summarize priority actions, and plan follow-up. Results are decision support only and require clinical review before diagnosis or care decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive health records are sent to a remote LLM endpoint. <br>
Mitigation: Use only de-identified data unless the endpoint is trusted and covered by an appropriate data-processing arrangement. <br>
Risk: The skill may save screening results to a local output file. <br>
Mitigation: Treat output files as sensitive medical records and apply local access controls, retention limits, and deletion procedures. <br>
Risk: Screening output may be mistaken for a clinical diagnosis. <br>
Mitigation: Use results as decision support for public health staff and require qualified clinical review for diagnosis or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-chronic-screening) <br>
- [Publisher profile](https://clawhub.ai/user/unisound-llm) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Text, Files] <br>
**Output Format:** [JSON followed by a natural-language summary; optionally written to a UTF-8 output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The output may contain sensitive medical screening results and should be access-controlled and retained according to local policy.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
