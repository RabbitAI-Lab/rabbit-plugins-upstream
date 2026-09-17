## Description:

This skill analyzes Chinese spoken-video transcripts offline and reports script structure, hook strength, retention pacing, speakability score, CTA strength, and the first three graded issues available in the free version.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, social media operators, and agents use this skill to evaluate spoken-word short-video scripts for structure, hook quality, pacing, speakability, and call-to-action strength before publishing or revising content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary flags under-disclosed paid-upgrade installation and purchase instructions.

Mitigation: Review any upgrade prompt before acting, and do not let an agent run the SkillPay installer or start purchase steps unless the source and separate paid product have been independently verified.

Risk: The free CLI creates a temporary marker used to limit repeated upsell prompting despite claiming stdout-only behavior.

Mitigation: Run it only where that local temp-file side effect is acceptable, and remove the marker or use an isolated environment when a clean local state is required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/viral-script-free)
- [Hook pattern reference](references/hook-patterns.md)
- [Platform pacing reference](references/platform-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Human-readable Chinese console report or JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The free version shows the overview, structure map, and first three issue titles; detailed positions, rule rationale, suggestions, golden-line candidates, and rewrite blueprint are withheld for the paid version.]

## Skill Version(s):

1.0.12 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
