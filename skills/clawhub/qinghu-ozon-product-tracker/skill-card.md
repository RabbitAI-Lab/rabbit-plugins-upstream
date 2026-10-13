## Description:

Tracks Ozon product price changes, reviews, ratings, competing sellers, and variants by product ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and analysts use this skill to review a product's recent price, review, rating, competing-seller, and variant history before making merchandising decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can install qhkit and Node/npm tooling on the host.

Mitigation: Review installation steps and prefer a preinstalled, pinned qhkit version.

Risk: Configuring long-lived API credentials can expose a token through shell history or configuration files.

Mitigation: Provide credentials through a secure secret mechanism rather than command-line arguments or persistent shell configuration.

Risk: Product-tracking queries consume credits, and costs can rise with result volume.

Mitigation: Check the current estimate, disclose that actual credits vary, and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-product-tracker)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Guidance]

**Output Format:** [Concise text or Markdown findings with an optional table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source period and sample size, key previews, and credits consumed for paid queries.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
