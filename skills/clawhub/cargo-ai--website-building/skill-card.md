## Description:

Builds and hosts a company website on its own domain using a static Next.js site on Cargo, with changes reviewed through pull requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and developers use this skill to build or update a company website, review changes in pull requests, and publish it on a company domain through Cargo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DNS changes could replace an existing www record or apex redirect.

Mitigation: Review the domain plan and obtain explicit approval for every replacement or deletion before deployment.

Risk: A domain purchase can incur a non-refundable charge, and a deploy may publish unreviewed content.

Mitigation: Confirm the price and require explicit approval for purchases; publish only through reviewed changes and an approved deployment plan.

Risk: Website build output is public and could expose sensitive data.

Mitigation: Keep credentials and private content out of website source and inspect the built output before publishing.

Risk: Outdated web dependencies or unpinned tooling could introduce vulnerabilities.

Mitigation: Audit and update pinned dependencies and any latest-version tooling before production use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/website-building)
- [Project homepage listed in skill metadata](https://github.com/getcargohq/gtm-skills)
- [Build and review guide](references/build-and-review.md)
- [Design-system capture guide](references/design-system-capture.md)
- [Domain and DNS guide](references/domain.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Guidance, Shell commands]

**Output Format:** [Website source files and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static Next.js website with domain configuration, subject to review before deployment.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
