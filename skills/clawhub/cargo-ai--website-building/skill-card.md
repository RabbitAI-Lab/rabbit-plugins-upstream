## Description:

Helps developers build a company website on Cargo using a statically exported Next.js app, a custom domain, and reviewed pull requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing teams use this skill to create or update a company website, prepare hosting and domain configuration, and submit changes for review before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Replacing a domain's DNS zone can remove mail records and interrupt email delivery.

Mitigation: Check for mailboxes, keep DNS at its current provider when needed, and review all records in the deployment plan.

Risk: A domain purchase or deployment can incur charges or publish unapproved content.

Mitigation: Review the pull request and plan, check price and available credits, and require explicit approval before purchase or deployment.

Risk: Website builds are public and can expose private content or credentials.

Mitigation: Keep secrets and private data out of the app and inspect the built site before publishing.

Risk: A deployment may appear successful before domain verification finishes.

Mitigation: Verify the domain records and live hostname, and report pending verification as pending.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/cargo-ai/skills/website-building)
- [Project homepage (listed in release metadata)](https://github.com/getcargohq/gtm-skills)
- [Build and review guide](references/build-and-review.md)
- [Design-system capture guide](references/design-system-capture.md)
- [Domain and DNS guide](references/domain.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown guidance with TypeScript/TSX and JSON website files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Website changes are prepared for review; deployment requires explicit approval.]

## Skill Version(s):

0.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
