## Description:

Helps build and host a company website on its own domain with Cargo, using a static Next.js site and reviewed changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing teams use this skill to adapt a company website, prepare its hosting and domain configuration, and submit changes for review before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A website or DNS change could replace an existing site or domain record.

Mitigation: Review the plan and DNS diff before deployment; obtain separate approval for DNS replacement.

Risk: Registering a new domain can incur a non-refundable charge.

Mitigation: Require explicit approval before any domain purchase.

Risk: Unpinned or outdated tool and dependency versions may affect production builds.

Mitigation: Update or pin the reported tool and dependency versions before production use.

## Reference(s):

- [Website Building on ClawHub](https://clawhub.ai/cargo-ai/skills/website-building)
- [Publisher-provided project homepage](https://github.com/getcargohq/gtm-skills)
- [Build and review guide](artifact/references/build-and-review.md)
- [Domain and DNS guide](artifact/references/domain.md)
- [Design-system capture guide](artifact/references/design-system-capture.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Markdown guidance, Shell commands]

**Output Format:** [Website source and configuration files, with review and deployment guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Changes are prepared for review; deployment and domain changes require operator approval.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
