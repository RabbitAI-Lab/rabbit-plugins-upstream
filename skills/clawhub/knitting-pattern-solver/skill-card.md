## Description:

Parse, decode, and expand written knitting patterns. Translates abbreviations, calculates yarn requirements from gauge, tracks stitch counts across rows, and generates row-by-row instructions from condensed pattern notation. Use when a knitter needs help understanding, planning, or tracking a knitting project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Knitters, yarn shop staff, and pattern designers use this skill to expand written knitting notation, estimate yarn needs from gauge data, and check stitch-count math before or during a project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Knitting calculations can be incorrect if the source pattern, user-entered gauge, or swatch measurements are wrong.

Mitigation: Check the original pattern, make and measure a gauge swatch, and verify stitch counts before relying on yarn estimates.

Risk: Yarn requirements may vary with tension, blocking, substitutions, and dye-lot availability.

Mitigation: Use the recommended safety buffer and buy enough yarn from the same dye lot when possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/knitting-pattern-solver)
- [Publisher Profile](https://clawhub.ai/user/voronindenis5)
- [Server-resolved GitHub Source](https://github.com/voronindenis5/knitting-pattern-solver)
- [Knitting Pattern Notation Reference](references/notation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with plain-text calculations and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-supplied pattern text and gauge values; yarn estimates include a configurable safety buffer.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
