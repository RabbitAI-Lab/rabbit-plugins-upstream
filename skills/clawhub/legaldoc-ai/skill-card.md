## Description: <br>
LegalDoc AI automates legal document review by extracting contract clauses, summarizing legal documents, assisting legal research, and tracking deadlines for law firms and legal professionals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manas-io-ai](https://clawhub.ai/user/manas-io-ai) <br>

### License/Terms of Use: <br>
Commercial <br>


## Use Case: <br>
Attorneys, paralegals, legal operations teams, and other legal professionals use this skill to accelerate contract review, legal document summarization, research workflows, and deadline management while preserving human legal judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Privileged or sensitive client facts may be exposed through external legal research queries. <br>
Mitigation: Avoid including privileged client facts in research prompts and configure research providers only after confirming data handling requirements. <br>
Risk: Deadline data may be stored locally in ~/.legaldoc/deadlines.db. <br>
Mitigation: Restrict local file access, apply appropriate retention controls, and periodically delete the local deadline database when it is no longer needed. <br>
Risk: Summaries, clauses, citations, and deadlines may be incomplete or incorrect. <br>
Mitigation: Independently verify all generated legal analysis and deadlines against source documents, applicable law, and professional legal judgment before relying on them. <br>
Risk: Some deadline rules are California-specific. <br>
Mitigation: Confirm jurisdiction-specific deadline and statute-of-limitations rules before using deadline outputs outside the supported jurisdiction. <br>


## Reference(s): <br>
- [LegalDoc AI ClawHub Listing](https://clawhub.ai/manas-io-ai/skills/legaldoc-ai) <br>
- [Full Documentation](https://docs.legaldoc.ai) <br>
- [API Reference](https://docs.legaldoc.ai/api) <br>
- [Clause Type Glossary](https://docs.legaldoc.ai/clauses) <br>
- [Integration Guides](https://docs.legaldoc.ai/integrations) <br>
- [Best Practices](https://docs.legaldoc.ai/best-practices) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text, Markdown, JSON, tables, and YAML configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include extracted clauses, document summaries, legal research results, deadline lists, suggested revisions, citations, alerts, and configuration values.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
