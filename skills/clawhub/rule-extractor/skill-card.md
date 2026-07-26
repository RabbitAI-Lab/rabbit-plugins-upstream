## Description: <br>
Rule Extractor derives avoid and prefer rules from trace records and .learnings markdown notes for reuse in later agent system prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to extract reusable behavioral rules from successful and failed operations, then format those rules as prompt text, JSON, or Markdown for review and integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated rules may be incorrect or misleading if they are added directly to an agent system prompt. <br>
Mitigation: Review generated rules before reuse and keep only guidance that is accurate for the target workflow. <br>
Risk: Running the extractor over untrusted, private, or attacker-controlled notes may expose sensitive content or turn hostile notes into prompt guidance. <br>
Mitigation: Use trusted input directories, avoid private or attacker-controlled notes, and review extracted rules before integration. <br>


## Reference(s): <br>
- [Rule Categories](references/rule_categories.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/rule-extractor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, guidance] <br>
**Output Format:** [System prompt text, JSON, or Markdown generated from extracted rule objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Rules include category, description, confidence, and source count when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
