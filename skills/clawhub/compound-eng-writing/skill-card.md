## Description: <br>
Prose editing, rewriting, and humanizing text for natural tone, or auditing a draft for AI tells without rewriting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and writing reviewers use this skill to rewrite or audit copy, docs, blog posts, emails, README text, and PR descriptions for natural tone while preserving the writer's voice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can over-edit prose or strip a writer's voice because it applies opinionated style rules. <br>
Mitigation: Review edits against the original draft and preserve natural passages; use the skill's restraint and recognizability checks. <br>
Risk: Detect mode can be mistaken for proof of AI authorship. <br>
Mitigation: Treat detections as pattern evidence only; do not use the output as an authorship verdict. <br>
Risk: Rewriting docs or PR descriptions can introduce incorrect technical claims, broken links, or wrong issue references if accepted without review. <br>
Mitigation: Review corrected text against source facts, links, issue IDs, and commands before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-writing) <br>
- [Specification](SPEC.md) <br>
- [Two-Phase Audit Workflow](references/audit-workflow.md) <br>
- [Before/After Examples](references/examples.md) <br>
- [Extended Phrase Reference](references/phrases.md) <br>
- [PR and MR Description Style](references/pr-descriptions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with audit notes, corrected prose, and changelog sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May quote short offending snippets in detect mode; does not run tools or code.] <br>

## Skill Version(s): <br>
4.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
