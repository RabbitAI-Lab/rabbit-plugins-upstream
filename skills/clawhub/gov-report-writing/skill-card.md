## Description: <br>
Gov Report Writing helps agents draft and review Chinese official reports and public-sector documents using GB/T 9704-2012 formatting guidance, report templates, vocabulary checks, policy citation cautions, and confidentiality safeguards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mogician11111](https://clawhub.ai/user/mogician11111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users use this skill to prepare Chinese government, state-owned-enterprise, and public-sector reports, summaries, meeting minutes, notices, requests, replies, and related formal documents. It guides agents to use templates, placeholders, local document generation, policy citation checks, and review steps before submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Classified, confidential, or sensitive internal raw material could be provided to the agent or reflected in a draft. <br>
Mitigation: Do not provide classified, confidential, or sensitive internal material; use placeholders, require desensitized inputs, and review every draft before submission. <br>
Risk: Generated facts, dates, names, policy citations, or official-document formatting may be incorrect. <br>
Mitigation: Review all factual claims and policy references against approved sources, replace placeholders manually, and use the bundled format checker for DOCX outputs when applicable. <br>
Risk: The skill may activate for a generic writing request where PRC/SOE-style official-document drafting is not intended. <br>
Mitigation: Ask the agent to use a general writing mode unless the user explicitly wants PRC/SOE-style official document drafting. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/mogician11111/skills/gov-report-writing) <br>
- [GB/T 9704-2012 formatting reference](artifact/references/gb-t9704-format.md) <br>
- [Report templates](artifact/references/report-templates.md) <br>
- [Vocabulary and wording guide](artifact/references/vocabulary-guide.md) <br>
- [Policy citation database](artifact/references/policy-database.md) <br>
- [AI trace review guide](artifact/references/ai-traces.md) <br>
- [DOCX format checker](artifact/scripts/format_check.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese report drafts, Markdown or HTML previews, Word document formatting instructions, and format-check command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses XX placeholders for missing or sensitive details and requires human review of facts, dates, names, policy citations, fonts, and formatting before submission.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata; artifact SKILL.md frontmatter states 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
