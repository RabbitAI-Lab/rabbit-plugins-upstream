## Description:

Museum Explorer helps agents create verified pre-visit museum curation cards, on-site checklists, and post-visit digital journals with stamp-style exhibit records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Museum visitors, cultural-travel planners, and agents supporting exhibition visits use this skill to plan a visit, answer on-site exhibit questions, and turn visit notes into a reusable local journal. It is especially tailored to Chinese-language museum workflows with source checks, exhibit keys, and stamp-style visit records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates and updates local journal and data files that may contain personal notes or photo references.

Mitigation: Tell users when local files are written and avoid storing sensitive personal notes or private photos unless the user is comfortable keeping them in the local journal folder.

Risk: Museum hours, tickets, exhibition dates, and exhibit facts can change or conflict across sources.

Mitigation: Use the bundled source-verification guide, record the information retrieval date, and mark unresolved or single-source facts as pending.

Risk: The skill may fetch public museum and source-verification pages during visit planning.

Mitigation: Limit browsing to public museum or verification sources needed for the user request and present source status in the generated outputs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bonniegeng-max/skills/museum-explorer)
- [Source verification guide](artifact/references/source-verification.md)
- [Museum data sources](artifact/references/data-sources.md)
- [Stamp design guide](artifact/references/stamp-design-guide.md)
- [Exhibit record schema](artifact/references/exhibits.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, SVG, JSON, Guidance]

**Output Format:** [Chinese-language guidance plus local Markdown, HTML, SVG, and JSON-backed files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local journal/session files and uses source-verification tables for museum facts.]

## Skill Version(s):

1.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
