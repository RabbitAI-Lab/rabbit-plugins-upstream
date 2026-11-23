## Description:

Manage Vercel, Cloudflare, and Fastly WAF firewall rules as code with the Doorman CLI. Use for any firewall-as-code task — creating rules, IP blocking, rate limiting, bot protection, geo-blocking, syncing local config to providers, validating configurations, exporting documentation, CI/CD automation, or translating rules between provider formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gfargo](https://clawhub.ai/user/gfargo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use Doorman to create, validate, compare, deploy, and document firewall rules as code across supported providers. The artifact also includes a Google Cloud Armor reference guide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious, citing command-execution risk in a privileged workflow and Google Cloud operations beyond the stated scope.

Mitigation: Before installing, review the CI workflow and any use of the unpinned package, and confirm the intended Google Cloud operations.

Risk: ClawScan reports incomplete validation guidance and a partial scan because three local references were unresolved.

Mitigation: Verify firewall configurations carefully and review the unresolved references before relying on the scan.

## Reference(s):

- [Server-resolved Doorman source (skills/doorman)](https://github.com/gfargo/doorman/tree/main/skills/doorman)
- [Doorman project](https://github.com/gfargo/doorman)
- [Rules reference](references/rules.md)
- [Cloudflare provider reference](references/cloudflare.md)
- [Fastly provider reference](references/fastly.md)
- [Google Cloud Armor provider reference](references/gcp.md)
- [CI/CD and automation reference](references/cicd.md)
- [Templates reference](references/templates.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON, YAML, and Terraform examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provider-specific instructions and examples for firewall rule workflows]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
