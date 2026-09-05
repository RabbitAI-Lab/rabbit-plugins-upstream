## Description:

詹明明·重讲一个概念 helps an agent prepare Chinese short-form concept-reframing scripts by locking the core question, definition, theory target, and analogies before drafting, then preserving the creator's spoken revision path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese content creators and their supporting agents use this skill to turn an already familiar concept into a short-form knowledge script. It guides the agent through topic qualification, one-page concept locking, drafting, spoken rewrite handling, review, cover handoff, filing, and follow-up measurement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow expects access to local content-planning, draft, cover, published-record, and follow-up files.

Mitigation: Install it only in workspaces where that vault access is intended, and review the expected paths before use.

Risk: Broad trigger phrases may route concept-explanation requests into this specialized production workflow.

Mitigation: Confirm the user wants the zmm/Douyin-style concept script workflow before allowing the skill to read or update local planning files.

Risk: Draft or review output could add incorrect or misleading content to scripts if accepted without review.

Mitigation: Review generated drafts, red-line checks, and follow-up records before publishing or filing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-concept)
- [锁四样](references/锁四样.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown guidance, checklists, tables, and draft-script text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language workflow output for concept selection, script drafting, review, publishing handoff, and measurement follow-up.]

## Skill Version(s):

0.2.4 (source: server release evidence; artifact frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
