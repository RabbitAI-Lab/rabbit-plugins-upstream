## Description: <br>
Audits a document against user-provided sources by extracting factual claims, grading each as evidenced, partially evidenced, unsupported, or contradicted, and identifying the source line behind the grade. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, reviewers, analysts, and teams use this skill to fact-check reports, decks, memos, posts, or pages against the sources supplied with them. It produces a claim ledger, ranked unsupported or contradicted claims, fix-or-drop recommendations, and an honesty score. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Claims may be marked unsupported when the user does not provide the relevant source material, even if those claims are true elsewhere. <br>
Mitigation: Provide the document and all source material to be checked, then review the claim ledger and source-line citations before relying on the audit. <br>


## Reference(s): <br>
- [Receipts Audit homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/receipts-audit.html) <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/receipts-audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report with tables and scored audit sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a claim ledger, load-bearing failure ranking, fix-or-drop register, and honesty score calculation.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
