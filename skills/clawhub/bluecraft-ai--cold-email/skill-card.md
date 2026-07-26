## Description: <br>
Build cold email campaigns and generate hyper-personalized email sequences with MachFive. Build a campaign end-to-end, preview output, then generate sequences from lead data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecraft-ai](https://clawhub.ai/user/bluecraft-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and sales teams use this skill to build MachFive cold email campaigns, configure required generation settings, preview results, and generate personalized outbound email sequences from lead data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lead and sender information is sent to MachFive for campaign building, enrichment, preview, and email generation. <br>
Mitigation: Use only lead data the user is allowed to share, review applicable privacy and email obligations, and enable enrichment only when company, website, or LinkedIn data sharing is appropriate. <br>
Risk: Preview and generation calls can spend MachFive account credits. <br>
Mitigation: Confirm the expected credit cost before preview or generation, including the higher per-lead cost when enrichment is enabled. <br>
Risk: The skill requires MACHFIVE_API_KEY for authenticated API calls. <br>
Mitigation: Store MACHFIVE_API_KEY as an environment secret and do not place it in chat messages, source files, or generated artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bluecraft-ai/skills/cold-email) <br>
- [MachFive API key settings](https://app.machfive.io/settings) <br>
- [MachFive application](https://app.machfive.io) <br>
- [MachFive product site](https://machfive.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown guidance with API request examples, shell polling commands, and generated email sequence text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MACHFIVE_API_KEY and may call MachFive APIs that process lead and sender information.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
