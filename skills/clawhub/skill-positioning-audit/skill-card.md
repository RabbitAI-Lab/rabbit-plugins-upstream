## Description:

Reviews a skill storefront position and produces an evidence-based Storefront Copy Brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this skill when a ClawHub skill page has unclear audience, promise, differentiation, or page hierarchy. It turns positioning evidence into a Storefront Copy Brief for downstream copywriting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release declares an unpinned Node.js CLI dependency that can change after publication.

Mitigation: Pin and integrity-verify the dependency before installation, or remove the CLI requirement if the positioning-review workflow does not need it.

Risk: Positioning recommendations can overstate claims when source evidence is incomplete.

Mitigation: Keep unsupported facts in open_questions and prohibit downstream copy from adding claims outside the Storefront Copy Brief.

## Reference(s):

- [Storefront Rubric](artifact/references/storefront_rubric.md)
- [Positioning Review Template](artifact/templates/positioning_review.md)
- [Weak vs Strong Positioning Example](artifact/examples/weak_vs_strong_positioning.md)
- [OpenClaw publisher homepage from clawdis metadata](https://github.com/bonniegeng-max/openclaw-publisher)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review findings and Storefront Copy Brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes positioning conclusion, audience, trigger, promise, differentiation pillars, evidence, page hierarchy, prohibited claims, and open questions.]

## Skill Version(s):

2.0.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
