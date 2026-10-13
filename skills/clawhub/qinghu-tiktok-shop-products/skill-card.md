## Description:

Queries products indexed for a TikTok Shop seller ID using the Qinghu data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and analysts use this skill to list products indexed for a TikTok Shop seller ID and review competing shops' assortments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit may change local Node tooling.

Mitigation: Review the installation before authorizing it and prefer a preinstalled or pinned qhkit version.

Risk: Product lookups can consume Qinghu credits, with higher charges for larger results.

Mitigation: Check the current estimate and obtain user consent before paid calls or large batches.

Risk: The lookup requires a Qinghu API token.

Mitigation: Provide the token through the supported configuration or environment variable and avoid exposing it in shared output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-tiktok-shop-products)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise summary and product preview; spreadsheet file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credits consumed for paid calls; larger results may be supplied as a local file.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
