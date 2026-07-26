## Description: <br>
Generates a standard discharge record from de-identified inpatient records by calling a medical language model and returning seven structured discharge-record fields. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical workflow developers and authorized medical-record operators use this skill to draft standardized discharge records from inpatient admission notes, progress notes, and discharge-related source text. The generated record is intended for review by licensed clinical staff before use in care, billing, archival, or handoff workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive patient records and sends prepared clinical text to a model endpoint. <br>
Mitigation: Use only de-identified records, an approved HTTPS endpoint, and an authorized app key; confirm local policy allows the transfer before use in clinical or regulated environments. <br>
Risk: Prepared input text and generated discharge records can be persisted through output paths or the save-prepared option. <br>
Mitigation: Avoid saving prepared text or outputs unless local storage is approved, access-controlled, and covered by a clear retention policy. <br>
Risk: Generated discharge records may be incomplete or unsuitable for direct clinical use without review. <br>
Mitigation: Require licensed clinical review against the source record before using the output for care, billing, archival, referral, or handoff workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-discharge-record) <br>
- [Unisound-LLM publisher profile](https://clawhub.ai/user/unisound-llm) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files] <br>
**Output Format:** [UTF-8 discharge-record text with seven Markdown-style sections; optional file output when an output path is supplied.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an input record file and an authorized app key for the configured medical model endpoint.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
