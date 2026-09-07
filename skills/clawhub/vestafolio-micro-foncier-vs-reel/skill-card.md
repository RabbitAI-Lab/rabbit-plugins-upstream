## Description:

Compares French unfurnished rental taxation under micro-foncier and regime reel with deficit foncier by collecting required inputs, calling Vestafolio's simulator API, and explaining the returned recommendation, savings, and limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to compare micro-foncier and regime reel taxation for unfurnished French rental income. It helps collect the simulator inputs, call the official Vestafolio calculation endpoint, and present concise guidance with caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends rental and tax figures to Vestafolio to complete the simulation, and the security evidence notes no explicit consent checkpoint.

Mitigation: Before the API request, ask the user to confirm the exact fields that will be sent and wait for approval; avoid unnecessary personal or identifying details.

Risk: The simulator covers a narrow tax scenario: unfurnished rentals in France using the coded 2025-2026 rules.

Mitigation: Keep recommendations within that scope, state that estimates are not tax advice, and direct furnished rentals, capital gains, or non-French rental income to other support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-micro-foncier-vs-reel)
- [Vestafolio interactive simulator](https://www.vestafolio.com/simulateurs/micro-foncier-vs-reel)
- [Vestafolio simulator API](https://www.vestafolio.com/api/tools/v1/micro-foncier-vs-reel)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise explanatory prose and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Grounded in the Vestafolio simulator result when network execution is available; otherwise the skill should state that calculation could not be completed.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter declares 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
