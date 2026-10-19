## Description:

Searches Chinese design patents by product name and Locarno class, then prepares a comparison list and representative images for product-design review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Product designers and teams researching existing Chinese design patents before launching a product can compare patent records and representative images. This is a screening aid, not an infringement opinion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries, product names, and design details are sent to a third-party patent service.

Mitigation: Obtain approval before submitting confidential or pre-launch designs; review the service before installation.

Risk: Searches and image retrieval may incur paid API charges, and a trial key may be stored locally.

Mitigation: Set a spending limit, monitor usage, and safeguard locally stored credentials.

Risk: A changed API endpoint could redirect patent queries or credentials.

Mitigation: Keep PATENTMAX_BASE_URL unset or confirm it points only to the intended PatentMax API.

Risk: Name-based searches and representative images can miss relevant designs or obscure differences.

Mitigation: Review complete patent views with a qualified professional before making infringement or patentability decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ip930/skills/design-patent-search)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Search workflow](references/search-workflow.md)
- [Query syntax](references/query-syntax.md)

## Skill Output:

**Output Type(s):** [Text, Files, Images]

**Output Format:** [Markdown summary, UTF-8 CSV comparison list, and representative image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source patent numbers and a link to the PatentMax search; images are representative, not complete patent views.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
