## Description:

A consulting delivery skill that turns user materials into structured storylines, strategy documents, PowerPoint decks, and speaker notes using a gated research, storyline, visualization, and review workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[forrestneo](https://clawhub.ai/user/forrestneo)

### License/Terms of Use:

MIT

## Use Case:

External consultants, business teams, and agent users use this skill to structure ambiguous business questions, fill evidence gaps with sourced research, and produce consulting-style storylines, decks, strategic documents, and speech drafts. It is intended for workflows where users can review source quality, storyline logic, and generated presentation materials before sharing them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can process uploaded consulting materials that may contain client-sensitive or regulated information.

Mitigation: Use it only in environments approved for the data being processed, avoid providing secrets or regulated client data unless permitted, and review generated deliverables before distribution.

Risk: The skill may use web searches and external sources to fill evidence gaps, which can introduce stale, weak, or mismatched evidence.

Mitigation: Review citations, source authority, dates, and stated assumptions before relying on generated analysis or sharing decks.

Risk: Generated PowerPoint decks and speech materials can contain visual, factual, or interpretation errors.

Mitigation: Apply the skill's storyline confirmation gate and critic checklist, then manually review final decks, scripts, and source footnotes before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/forrestneo/skills/mckinsey-library)
- [Server-resolved GitHub provenance](https://github.com/forrestneo/mckinsey-library)
- [README](README.md)
- [Methodology](references/methodology.md)
- [External research](references/external_research.md)
- [Storyline template](references/storyline_template.md)
- [Visualization layouts](references/visualization_layouts.md)
- [Layout selection](references/layout_selection.md)
- [Critic checklist](references/critic_checklist.md)
- [PPTX primitives](assets/pptx_primitives.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, PowerPoint files, Python generation code, shell commands, and consulting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sourced research notes, storyline drafts, presentation decks, strategy documents, speech drafts, and visual quality review notes.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter says 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
