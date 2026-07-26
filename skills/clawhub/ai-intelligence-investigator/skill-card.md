## Description: <br>
A-share intelligence investigation assistant for company research, competitor analysis, sentiment and event tracking, background checks, and multi-source information verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users such as investors, product and marketing teams, content operators, journalists, business development teams, and researchers use this skill to gather public information, cross-check claims, and produce structured investigation reports with source and credibility annotations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated investigation reports may be sent to and stored by RedFox automatically when an API key is configured. <br>
Mitigation: Use the skill only for reports that are appropriate to store with RedFox, and avoid confidential, regulated, personal, or sensitive business investigations unless RedFox access, retention, deletion, and revocation controls are understood. <br>
Risk: The skill requires REDFOX_API_KEY for RedFox record saving, which can expose account access if mishandled. <br>
Mitigation: Keep the key in environment variables, do not hard-code or print it in prompts, logs, code, or output files, and confirm that the key can be reset or revoked. <br>
Risk: Financial, background, and reputation reports can contain incomplete or misleading public-source findings. <br>
Mitigation: Review source notes and credibility labels, cross-check important conclusions, and treat A-share outputs as informational rather than investment advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/ai-intelligence-investigator) <br>
- [Core Workflow](references/core_workflow.md) <br>
- [Investigation Modes](references/investigation-modes.md) <br>
- [Engine Strategy](references/engine-strategy.md) <br>
- [Investigation Templates](references/investigation-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Shell commands, Guidance] <br>
**Output Format:** [Structured Markdown investigation reports with tables, source notes, credibility labels, and optional shell commands for RedFox record saving] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may be automatically sent to RedFox when REDFOX_API_KEY is configured.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
