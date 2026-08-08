## Description: <br>
Travel Assistant helps an agent organize travel plans, identify common missed details such as visas, weather, cultural norms, and packing needs, and produce itinerary and preparation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-planning agents use this skill to summarize trip details, surface preparation gaps, and generate practical checklists or travel guidance. It is intended for ordinary planning support, not for final legal, immigration, safety, or medical decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad file and shell-command authority for a travel-planning use case. <br>
Mitigation: Run it only in a constrained agent environment, require explicit confirmation before writes or commands, and prefer an allowlist or a version without exec authority. <br>
Risk: Travel guidance can become outdated or incomplete for visas, entry rules, severe weather, and local restrictions. <br>
Mitigation: Verify time-sensitive travel requirements with official sources before booking or traveling. <br>
Risk: Trip planning may involve sensitive personal data such as passport details, identity numbers, payment information, and API keys. <br>
Mitigation: Share the minimum necessary personal information, redact secrets from prompts and outputs, and avoid storing sensitive travel documents in skill-generated files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/travel-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce travel overviews, todo lists, packing checklists, weather reminders, visa reminders, troubleshooting notes, and setup guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter says 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
