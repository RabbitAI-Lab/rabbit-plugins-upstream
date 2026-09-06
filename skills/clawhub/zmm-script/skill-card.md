## Description:

A collaborative Chinese talking-head script writing skill for knowledge-commerce creators that selects script types, assembles content units, and co-writes drafts section by section instead of producing a one-shot script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing agents use this skill to develop Chinese knowledge-commerce talking-head video scripts, including script-type selection, opening hooks, two-column storyboard drafts, alternate hooks, and concrete material collection checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist user feedback, generated drafts, and derived writing rules into long-lived local libraries or memory.

Mitigation: Use it only in a trusted personal vault and require explicit review before writes to draft, framework, content-library, feedback, or memory folders.

Risk: The workflow references a local index-rebuild script before comparing published content indexes.

Mitigation: Inspect the referenced local script before allowing it to run, and review any generated index changes before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-script)
- [概念型口播](references/概念型口播.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured tables, numbered options, inline file paths, draft sections, alternate hooks, and material collection checklists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow is interactive and section-by-section; when permitted, it can create or update draft, feedback, content-library, and memory files in the user's local vault.]

## Skill Version(s):

0.2.6 (source: release evidence; artifact frontmatter reports 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
