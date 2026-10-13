## Description:

Helps agents audit and improve websites for AI search visibility, including preview and static-site audits, regression comparisons, schema checks, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site owners use this skill to assess website visibility to AI systems, prioritize fixes, validate structured data, compare releases, and create AI-readable site files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Website audits can access local or private previews when explicitly enabled.

Mitigation: Audit only sites and local previews you are authorized to test; enable private-target access only on explicit request.

Risk: Generated llms.txt, llms-full.txt, or robots.txt changes may alter how crawlers access site content.

Mitigation: Review generated files and site fixes before committing or deploying them.

## Reference(s):

- [ClawHub AEO skill release](https://clawhub.ai/arberx/skills/aeo)
- [Canonry website](https://canonry.ai)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration files]

**Output Format:** [Markdown guidance, JSON audit reports, and text files such as llms.txt and robots.txt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or apply site fixes after user confirmation.]

## Skill Version(s):

7.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
