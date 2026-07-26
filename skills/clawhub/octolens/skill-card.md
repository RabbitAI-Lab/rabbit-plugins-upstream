## Description: <br>
Query and analyze brand mentions from the Octolens API across social, developer, and media platforms with filtering for source, sentiment, engagement, date range, keywords, tags, and saved views. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[garrrikkotua](https://clawhub.ai/user/garrrikkotua) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, support teams, and marketing or community operators use this skill to query Octolens mention data, analyze sentiment and engagement, and summarize brand or product conversations across monitored sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an Octolens API key and can query account data through the Octolens API. <br>
Mitigation: Use a least-privileged Octolens API key and provide it only when the agent needs to make an authorized request. <br>
Risk: Shell command examples can expose secrets if real API keys are pasted directly into terminal history or logs. <br>
Mitigation: Use a safer secret mechanism where available and avoid placing real API keys directly in command arguments. <br>
Risk: Mention exports may include business-sensitive customer, competitor, or campaign information. <br>
Mitigation: Treat retrieved mention data as sensitive and share summaries or raw results only with appropriate recipients. <br>


## Reference(s): <br>
- [Octolens Skill Page](https://clawhub.ai/garrrikkotua/skills/octolens) <br>
- [Octolens API Base URL](https://app.octolens.com/api/v1) <br>
- [Octolens API Usage Examples](references/EXAMPLES.md) <br>
- [Octolens Filter Reference Guide](references/FILTERS.md) <br>
- [Octolens Helper Scripts](scripts/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with inline JSON, JavaScript, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Octolens mention summaries, filter structures, pagination guidance, and command examples for bundled Node.js scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
