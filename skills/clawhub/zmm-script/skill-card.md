## Description:

Guides an agent through collaborative Chinese talking-head script writing for knowledge creators, using script-type selection, content-unit assembly, and section-by-section drafting instead of one-click full drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External knowledge creators and writing assistants use this skill to turn topics, source material, and feedback into Chinese talking-head scripts. It emphasizes collaborative drafting, concrete examples, citation discipline, and staged confirmation before completing a script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read broad vault content while assembling scripts.

Mitigation: Install and run it only with vaults and local source material the user trusts, and scope access to the intended workspace.

Risk: The skill may run local indexing scripts as part of its workflow.

Mitigation: Require confirmation before executing local Python scripts and review the command purpose before routine use.

Risk: The skill may write feedback, viewpoints, cases, or preferences into persistent content libraries or long-term memory.

Mitigation: Require confirmation before persistent writes and review resulting changes before sharing the workspace.

Risk: Generated scripts can become misleading if personal examples, citations, or source facts are missing.

Mitigation: Review factual claims, provide real source material, and stop rather than invent cases or numbers when evidence is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-script)
- [规则卡](artifact/references/规则卡.md)
- [概念型口播](artifact/references/概念型口播.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown script draft with sectioned notes and numbered options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include complete spoken-script text, evidence-shot notes, alternate hooks, and material collection checklists.]

## Skill Version(s):

0.2.9 (source: server release metadata; artifact frontmatter says 0.3.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
