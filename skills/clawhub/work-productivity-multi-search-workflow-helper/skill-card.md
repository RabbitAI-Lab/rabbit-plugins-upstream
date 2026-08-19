## Description:

Helps AI-agent users, skill authors, maintainers, and teams create practical workflows, artifacts, checklists, analyses, code changes, or decision support for multi-search-engine-style work productivity needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to turn multi-search-engine-style productivity requests into concise plans, templates, checklists, analyses, implementation support, and validation notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation keywords and implicit invocation can make the helper activate for unrelated search or workflow prompts.

Mitigation: Narrow the trigger keywords and disable implicit invocation unless broad automatic activation is intended.

Risk: Workflow guidance may be applied without checking whether it fits the user's concrete inputs and success criteria.

Mitigation: Restate assumptions, validate the result against the stated success criteria, and list remaining risks before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-multi-search-workflow-helper)
- [Requirement plan](references/requirement-plan.md)
- [Popular ClawHub skill demand: Multi Search Engine](https://clawhub.ai/skills/multi-search-engine)
- [Ask HN: How to tune Emacs config for portability](https://news.ycombinator.com/item?id=49349796)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional code blocks, shell commands, checklists, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, and remaining risks; the packaged skill is documentation-only.]

## Skill Version(s):

0.20260819.45504 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
