## Description:

Multi-page Lighthouse audit via the MIT-licensed Unlighthouse CLI. Free-tier alternative to running PageSpeed against every URL on a site, no API quota burn, runs locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and SEO engineers use this skill to run local multi-page Lighthouse audits, aggregate route-level scores, and support CI or post-deploy regression checks without PageSpeed API quota usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can crawl and audit user-supplied websites.

Mitigation: Use it only on sites you are authorized to crawl or audit, and keep route caps appropriate for the target site.

Risk: The workflow depends on a local Node 18+ environment and the Unlighthouse package or companion installer.

Mitigation: Review the installer and dependency setup before running it in a trusted local or CI environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/seo-unlighthouse)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples and parsed JSON audit results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated JSON and HTML reports from the configured Unlighthouse output directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
