## Description: <br>
Lunheng is an AI judgment-drafting assistant for Chinese legal documents with syllogistic reasoning, document drafting and revision, law-citation checking, quality scoring, sentencing calculation, batch processing, and case retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lawrencepage](https://clawhub.ai/user/lawrencepage) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Legal professionals and developers use this agent to draft, review, score, and refine Chinese judgment documents from case facts while checking citations, reasoning structure, fees, and sentencing guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive legal case text may be sent to configured LLM or API endpoints. <br>
Mitigation: Use a local or zero-retention endpoint for confidential matters and redact personal identifiers before drafting. <br>
Risk: Generated legal, citation, fee, or sentencing output may be incorrect or outdated. <br>
Mitigation: Have a qualified legal professional review all output against current authoritative law before use. <br>
Risk: The web UI may expose users to untrusted generated HTML. <br>
Mitigation: Avoid the web UI with untrusted generated HTML and review generated files before opening them in a browser. <br>
Risk: Privacy and logging behavior can vary across configured external services. <br>
Mitigation: Confirm endpoint retention and logging terms, limit access to local profile files, and avoid placing secrets in shared workspaces. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lawrencepage/skills/lunheng) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [Knowledge router](refs/knowledge_router.md) <br>
- [Legal knowledge base](refs/kb_laws.md) <br>
- [Formatting standard](refs/formatting_standard.md) <br>
- [Evaluation framework](refs/eval_framework.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, HTML, JSON, and shell-command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce legal-document drafts, review reports, quality scores, API responses, and generated files for downstream human review.] <br>

## Skill Version(s): <br>
3.0.5 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
