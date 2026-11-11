## Description:

Finds and evaluates human-made visual and audio references for AI image, video, and music work, then prepares candidates for human selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and production teams use this skill to find and assess human-made references for AI-generated or code-produced creative work. It organizes the research into a shortlist and supporting notes for a person to review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private images or creative briefs may be exposed if sent to hosted models before external processing boundaries are clear.

Mitigation: Avoid sending private images or briefs to hosted models until the external processing warnings and scope boundaries are clarified.

Risk: Unpinned packages or mutable image commands may change between review and use.

Mitigation: Review and pin packages and image commands before using them.

Risk: The available security scan is partial, and unresolved local references leave evidence incomplete.

Mitigation: Review the full skill and its unresolved local references before installation or use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/vargai/skills/find-references)
- [Declared project homepage (clawdis metadata)](https://github.com/vargHQ/skills/tree/main/find-references)
- [Reference query guide](artifact/references/queries.md)
- [Source access guide](artifact/references/sources.md)
- [Evidence guide](artifact/references/evidence.md)
- [Skill workflow and operating guidance](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, HTML, Reference links]

**Output Format:** [Markdown, JSON, JSONL, and HTML files with links to reference candidates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A candidate board and supporting query, evidence, and rights notes; contents vary by requested jobs.]

## Skill Version(s):

1.0.4 (source: target release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
