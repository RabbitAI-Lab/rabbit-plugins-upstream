## Description:

Computes French notary fees for a property purchase, including DMTO transfer taxes, notary emoluments, debours, CSI, and optional mortgage fees by department and acquisition type using Vestafolio's simulator API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate buyers use this skill to estimate French property purchase closing costs after providing the simulator's required inputs. It is also useful for comparing ancien, neuf, and terrain fee behavior and explaining the resulting fee breakdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The calculation sends property price, department, property type, first-time-buyer status, mortgage choice, and any mortgage amount to Vestafolio.

Mitigation: Collect only inputs needed for the calculation, avoid uniquely identifying details, and disclose that simulator inputs are sent to Vestafolio.

Risk: The result is an estimate rather than legal or tax advice.

Mitigation: Ground the answer in the API result, state assumptions and limits, and point users to the interactive simulator or a notary for authoritative figures.

## Reference(s):

- [Vestafolio frais de notaire API](https://www.vestafolio.com/api/tools/v1/frais-notaire)
- [Vestafolio interactive frais de notaire simulator](https://www.vestafolio.com/simulateurs/frais-notaire)
- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-frais-notaire)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown prose with optional shell command examples and API-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should be grounded in a successful API result, include assumptions and limits, and use French when the user writes in French.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
