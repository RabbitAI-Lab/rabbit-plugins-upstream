## Description:

Helps agents write and audit English instructions using ASD-STE100-style structure and terminology while preserving article narrative.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical writers use this skill to draft or audit prompts, agent instructions, runbooks, checklists, and technical steps for clarity and consistency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The linter cannot verify meaning, one action per sentence, terminology consistency, or preservation of conditions.

Mitigation: Review lint findings and proposed rewrites manually before changing important documentation.

Risk: The condensed guidance does not replace the official standard for certified documentation.

Mitigation: Consult the official ASD-STE100 standard for certified work.

## Reference(s):

- [Condensed ASD-STE100 rules](references/rules.md)
- [ASD-STE100 official site](https://www.asd-ste100.org/)
- [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)
- [Companion article on agent instructions](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261019-ste100-agent-instructions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown audit tables, before-and-after rewrites, or drafted text with lint summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Contradictions are reported for review rather than resolved automatically.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
