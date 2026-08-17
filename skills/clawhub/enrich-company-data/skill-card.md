## Description:

Enriches approved company lists with Cargo firmographics such as industry, size, geography, founding year, and headquarters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, go-to-market, and data operations teams use this skill to match companies to Cargo business IDs and enrich permitted company lists with firmographic fields before segmentation, analysis, or outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs Cargo session attribution outside the core company enrichment task.

Mitigation: Review the attribution behavior before installing and remove or decline the step if automatic Cargo attribution is not acceptable.

Risk: The skill asks to star a GitHub repository using the user's account after successful completion.

Mitigation: Proceed only after explicit user approval, and decline or remove this step when GitHub endorsement is not appropriate.

Risk: Company lists are sent to Cargo for matching and enrichment.

Mitigation: Use only company data that is approved for Cargo processing, sample 10 to 20 records first, and obtain approval before running a full batch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/enrich-company-data)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo GTM build TAM recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON command inputs or outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create matched.json and may invoke Cargo CLI batch operations when followed.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
