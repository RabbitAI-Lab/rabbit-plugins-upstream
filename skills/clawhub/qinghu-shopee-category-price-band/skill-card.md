## Description:

Helps analyze Shopee category price bands using Qinghu data on sales volume, revenue, product counts, and their shares.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and market analysts use this skill to identify leading price ranges in second- or third-level Shopee categories across supported sites and inform pricing decisions.

### Deployment Geography for Use:

Global (analysis covers supported Shopee sites in Taiwan, Malaysia, Indonesia, Thailand, the Philippines, Singapore, Vietnam, and Brazil)

## Known Risks and Mitigations:

Risk: The setup instructions can make lasting local changes by installing or upgrading unpinned tooling.

Mitigation: Prefer an approved, pinned or preinstalled qhkit version; review any installation or upgrade before proceeding.

Risk: Calls to the external Qinghu service require a token and may consume paid credits.

Mitigation: Confirm site, category, date, and estimated credits with the user before calling; handle the token securely and report actual credits used.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-price-band)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [Text or Markdown summary, with a table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results identify the Shopee site and reporting date; paid calls report credits consumed.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
