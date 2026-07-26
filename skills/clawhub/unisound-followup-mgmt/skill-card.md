## Description: <br>
Generates structured post-exam follow-up plans from health examination reports, including follow-up timing, review items, health guidance, alert conditions, and recipient-facing follow-up notices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Health examination centers and health management teams use this skill to turn patient examination reports into structured follow-up schedules and practical health coaching. The generated plan supports post-exam service workflows but should be reviewed by qualified medical staff before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Health report contents are sent to the configured remote LLM endpoint, which may expose sensitive health data if identifiers remain in the input. <br>
Mitigation: Remove names, IDs, phone numbers, addresses, and other direct identifiers before running the skill, and use it only when the remote endpoint is approved for the data involved. <br>
Risk: The documentation promises de-identification, but the security evidence says the script does not enforce it. <br>
Mitigation: Treat de-identification as a required pre-processing step outside the skill and review inputs before execution. <br>
Risk: Generated follow-up plans are health management guidance and may be incomplete or unsuitable for an individual case. <br>
Mitigation: Have qualified medical staff review the output before sharing it with recipients or using it in care workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-followup-mgmt) <br>
- [Configured LLM API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Markdown, Guidance] <br>
**Output Format:** [JSON followed by a plain-language follow-up notice] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the generated follow-up plan to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
