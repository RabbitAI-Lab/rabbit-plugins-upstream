## Description: <br>
Set up and use ViralQuery's protected HTTP API to build a private video inspiration feed for one app, website, or niche. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tfcbot](https://clawhub.ai/user/tfcbot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and external users can use this skill to configure ViralQuery access, create or update a research brief and rules, run a scroll, and retrieve tenant-scoped video research signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a ViralQuery API key and may send research briefs, rules, prompts, and source queries to ViralQuery. <br>
Mitigation: Store the API key in an environment secret store, avoid pasting credentials into chat, and confirm the research brief is appropriate for the service before running a scroll. <br>
Risk: Recurring research or overlapping scrolls could run when the user only intended one research pass. <br>
Mitigation: Use scheduling fields only when the user explicitly requests recurring research and avoid starting overlapping work for the same workspace. <br>
Risk: An incorrect or overridden API URL could send requests to an unintended service. <br>
Mitigation: Use https://api.viralquery.com unless a configured API URL is intentionally set, and verify credentials with the protected /v1/usage endpoint. <br>


## Reference(s): <br>
- [ViralQuery LLM documentation](https://viralquery.com/llms.txt) <br>
- [ViralQuery documentation](https://viralquery.com/docs) <br>
- [ViralQuery ClawHub skill page](https://clawhub.ai/tfcbot/skills/viralquery) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and API endpoint guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include bounded polling guidance, credential-handling steps, and source URLs from ViralQuery results.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
