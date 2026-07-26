## Description: <br>
Cctv News Tool Free helps agents retrieve CCTV Xinwen Lianbo titles and summaries for a specified date, classify items at a basic domestic/international level, and produce a concise briefing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual users, creators, and agents use this skill to fetch CCTV news items for a single date and turn the results into a basic categorized news brief. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution and includes unsafe installer guidance. <br>
Mitigation: Review each command before allowing execution, and prefer a trusted package manager or verified installer over curl-to-bash installation. <br>
Risk: Broad activation wording may cause the skill to activate for unrelated marketing or writing tasks. <br>
Mitigation: Limit activation and use to CCTV news retrieval, classification, and briefing workflows. <br>
Risk: The security verdict is suspicious because the release combines command execution with broad activation wording. <br>
Mitigation: Review and scan the skill before deployment, and install it only when CCTV news retrieval and briefing are intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cctv-news-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code examples, shell commands, and JSON-shaped news results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are oriented around single-date CCTV news retrieval, basic categorization, and concise briefing generation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
