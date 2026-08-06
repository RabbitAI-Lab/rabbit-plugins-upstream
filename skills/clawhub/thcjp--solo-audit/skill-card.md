## Description: <br>
Solo Audit helps agents check knowledge bases for broken links, missing frontmatter, tag inconsistencies, cover issues, and related remediation suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge-base maintainers, and automation teams use this skill to audit Markdown-style knowledge bases for link, metadata, tag, and cover consistency issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence marks the skill suspicious because it presents itself as a knowledge-base checker while also claiming broad security-audit capabilities and requesting command, file-write, and API-style authority without clear limits. <br>
Mitigation: Install only for supervised knowledge-base audits, restrict it to intended project directories, and require explicit confirmation before file writes, command execution, or external service calls. <br>
Risk: The skill documentation mentions API-key style configuration without a concrete integration. <br>
Mitigation: Do not provide sensitive API keys unless a specific integration and handling path are explained and reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/solo-audit) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown or JSON audit reports with findings, scores, and suggested improvements] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include issue summaries, per-item status, scores, and prioritized remediation guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.4.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
