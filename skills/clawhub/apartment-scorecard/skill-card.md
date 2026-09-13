## Description:

Helps renters compare apartments and rental homes by applying hard constraints, weighted scoring, true monthly cost modeling, affordability checks, side-by-side comparisons, and negotiation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to evaluate rental listings, estimate all-in monthly costs, screen against personal constraints, compare finalists, and prepare fact-based negotiation scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apartment listing and budget inputs may contain personal housing and financial details.

Mitigation: Review input files and generated reports before sharing them; the security evidence says inspected artifacts do not send this data off-machine.

Risk: The skill stores editable preferences in ~/.apartment-scorecard.json.

Mitigation: Inspect the local preferences file before screening listings, especially budget, commute, pet, bedroom, and move-date constraints.

## Reference(s):

- [Listing Format & Tour Protocol](references/listing-format.md)
- [Server-resolved source repository](https://github.com/voronindenis5/apartment-scorecard)
- [ClawHub skill listing](https://clawhub.ai/voronindenis5/skills/apartment-scorecard)
- [Publisher profile](https://clawhub.ai/user/voronindenis5)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with shell command examples and local JSON or CSV configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local rental analysis and decision guidance; no network output is described in the inspected artifacts.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
