## Description:

Guides Chinese knowledge creators through a concept-video drafting workflow that locks the core question, definition, theory target, and analogies before drafting and finalizes from the host's spoken version.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content teams use this skill to turn a familiar business or content concept into a short-form Chinese concept script. It helps lock the question, host-owned definition, theory target, and analogies before drafting, then supports spoken revision, red-line review, title/cover handoff, and release follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may lead an agent to update drafts, rule files, published-content indexes, calendar records, or frontmatter in a content vault.

Mitigation: Review proposed changes before allowing writes, and keep the vault under version control or another recoverable backup process.

Risk: Broad concept-explanation prompts may invoke this specialized Chinese content workflow when its triggers match.

Mitigation: Confirm that the zmm concept-script workflow and target content vault are intended before continuing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-concept)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [规则卡](references/规则卡.md)
- [锁四样](references/锁四样.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, draft text, checklists, and occasional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to content-vault drafts, rule files, published-content indexes, calendar records, and frontmatter.]

## Skill Version(s):

0.2.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
