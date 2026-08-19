## Description:

Looks up LCA emission factors, product carbon footprint data, BOM accounting inputs, industry benchmarks, production-route comparisons, and EPD peer data from HiQ Cortex and referenced life-cycle inventory sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kirbyingithub](https://clawhub.ai/user/kirbyingithub)

### License/Terms of Use:

MIT-0

## Use Case:

LCA practitioners, sustainability analysts, and agent developers use this skill to retrieve sourced emission-factor candidates, GWP values, cohort distributions, EPD results, and related basis details for carbon-footprint and life-cycle assessment work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LCA search terms, material names, and BOM lines are sent to HiQ's service for lookup.

Mitigation: Review inputs before use and avoid sending confidential product or supplier data unless that external service use is acceptable.

Risk: Browser sign-in creates a reusable local credential.

Mitigation: Use a scoped API key where appropriate, restrict use on shared machines, and run logout after completing the workflow.

Risk: The scanner reported under-disclosed install attribution metadata.

Mitigation: Confirm whether host, distribution channel, skill, and version attribution are acceptable before deployment.

## Reference(s):

- [HiQ Agent Skills Repository](https://github.com/HiQ-AI/agent-skills)
- [HiQ Cortex API](https://x.hiqlcd.com)
- [HiQ](https://www.hiqlcd.com/)
- [ClawHub Skill Page](https://clawhub.ai/kirbyingithub/skills/hiq-cortex)
- [Publisher Profile](https://clawhub.ai/user/kirbyingithub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and structured lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve database, version, system model, geography, reference unit, restriction status, and comparability notes when values are reported.]

## Skill Version(s):

1.8.3 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
