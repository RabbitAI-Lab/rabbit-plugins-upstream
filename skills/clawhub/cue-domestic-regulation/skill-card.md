## Description:

Searches Chinese domestic laws and regulations and summarizes relevant provisions, legislative context, and compliance points with source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal and compliance teams, businesses, and individuals use the skill to research Chinese domestic regulations, find cited provisions, and review compliance requirements or common legal questions. The resulting research is informational and should be checked against linked source materials.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Legal research results may be incomplete or mistaken and do not constitute legal advice.

Mitigation: Check cited provisions and current status against the linked official sources; seek qualified legal advice for decisions requiring it.

Risk: The workflow sends case details to Cue and may expose report links whose privacy depends on the service.

Mitigation: Send only case details suitable for sharing with Cue and check report-link privacy.

Risk: The workflow relies on changing external runner code and includes cancellation restrictions and promotional prompts.

Mitigation: Review and pin the external runner, preserve the ability to cancel tasks, and make promotional prompts optional.

Risk: The Cue API key could be exposed through chat or an inadequately protected configuration file.

Mitigation: Use a dedicated Cue key, avoid pasting it into chat, and restrict access to its configuration file.

## Reference(s):

- [Cue platform](https://cuecue.cn)
- [Cue Playbook](https://cuecue.cn/playbook)
- [Runner project referenced in the skill documentation](https://github.com/sensedeal/cue-skills)
- [National Laws and Regulations Database](https://flk.npc.gov.cn)
- [Ministry of Justice of the People's Republic of China](https://www.moj.gov.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese structured Markdown report with legal citations and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cited provisions and source links; coverage may be incomplete, and the report is not legal advice.]

## Skill Version(s):

1.0.11 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
