## Description: <br>
Drafts, rewrites, compresses, and reviews Chinese official documents and formal workplace materials, including requests, reports, notices, plans, minutes, speeches, institutional rules, procurement materials, and AI-compute service documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, administrators, and agents use this skill to draft or review Chinese official documents and formal work materials while preserving document genre, reporting relationship, factual boundaries, required handling elements, and formal tone. It is also useful for checking AI-like phrasing, incomplete placeholders, official-document format risks, and AI-compute procurement or service materials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect formal document text that the user provides, and an optional lint script can read local draft files when invoked. <br>
Mitigation: Use it only on documents the user intentionally provides or explicitly asks the lint script to inspect, and avoid sharing sensitive draft content unless the deployment environment is approved for that data. <br>
Risk: Generated official-document language can be mistaken for a final legal, financial, procurement, audit, or signing conclusion. <br>
Mitigation: Require human review for formal signing, legal, financial, procurement, audit, and approval decisions before use. <br>
Risk: Sparse prompts can lead to unsupported factual detail in formal documents if factual boundaries are not enforced. <br>
Mitigation: Keep drafts limited to user-provided facts and mark missing business facts for user confirmation instead of inventing organizations, dates, amounts, contacts, or decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Workflow](artifact/references/workflow.md) <br>
- [Genre routing](artifact/references/genre-routing.md) <br>
- [Handling elements](artifact/references/handling-elements.md) <br>
- [GB/T 9704 formatting](artifact/references/format-gbt9704.md) <br>
- [Review checklist](artifact/references/review-checklist.md) <br>
- [AI-compute document guidance](artifact/references/ai-compute-docs.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration] <br>
**Output Format:** [Plain text or Markdown, with optional code, shell command, or configuration snippets when the user asks for supporting files or checks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should stay within user-provided facts and avoid adding real organizations, policies, dates, amounts, contacts, signatures, approval conclusions, or other unsupported details.] <br>

## Skill Version(s): <br>
1.5.25 (source: server evidence release.version and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
