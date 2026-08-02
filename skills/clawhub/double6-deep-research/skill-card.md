## Description: <br>
Guides an agent through authorized multi-source research and produces a sourced report, research record, SHA-256 candidate hashes, validation receipt, and independent review workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[double6-ai](https://clawhub.ai/user/double6-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and research agents use this skill to plan and complete evidence-based research tasks, comparisons, decision support, and complex fact checking. It emphasizes scoped authorization, source coverage, report quality, validation receipts, and independent review before final acceptance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use web pages, local materials, and a delivery directory selected for the research task, so unclear authorization can expose sensitive or out-of-scope material. <br>
Mitigation: Confirm the allowed local materials and output directory before use, and stop or narrow the task when authorization is unclear. <br>
Risk: The validator checks local report structure, hashes, citations, coverage, and review records, but it does not independently verify source truth or research quality. <br>
Mitigation: Require careful human review for sensitive or high-stakes research, especially medical, legal, financial, compliance, or safety decisions. <br>
Risk: Unavailable or incomplete sources can leave claims unsupported or conclusions narrower than requested. <br>
Mitigation: Record evidence gaps, mark the research as partial or blocked when coverage cannot be completed, and avoid presenting unresolved claims as fully verified. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/double6-ai/skills/double6-deep-research) <br>
- [Double6 Deep Research Source Homepage](https://github.com/double6-ai/double6-skills/tree/main/skills/double6-deep-research) <br>
- [Report Quality Reference](artifact/references/report-quality.md) <br>
- [Privacy and Fail-closed Boundaries](artifact/references/privacy-and-fail-closed.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports, JSON audit records, validation receipts, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are scoped to the user-authorized delivery directory; the local validator checks report structure, hashes, citations, coverage, and review records.] <br>

## Skill Version(s): <br>
2.0.2 (source: SKILL.md frontmatter, CHANGELOG.md, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
