## Description:

Parse, decode, and expand written knitting patterns. Translates abbreviations, calculates yarn requirements from gauge, tracks stitch counts across rows, and generates row-by-row instructions from condensed pattern notation. Use when a knitter needs help understanding, planning, or tracking a knitting project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users, knitters, yarn shop staff, and pattern designers use this skill to decode written knitting notation, expand repeats, check stitch counts, and estimate yarn needs before or during a project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect stitch-count or yarn estimates could cause project delays, wasted materials, or rework.

Mitigation: Manually verify important calculations against the original pattern and a measured gauge swatch, and use the recommended safety buffer before buying yarn.

Risk: The skill is scoped to standard English written knitting notation and does not cover crochet, machine-knitting, or chart-only patterns.

Mitigation: Use it only for supported text-based knitting patterns and consult the source pattern or a domain reference for unsupported notation.

## Reference(s):

- [Knitting Pattern Notation Reference](references/notation.md)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/knitting-pattern-solver)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/knitting-pattern-solver)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with plain-text calculations and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include expanded row instructions, stitch-count checks, yarn estimates, skein recommendations, and safety-buffer guidance.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
