## Description:

Iran Chemical Database helps agents use a live, auditable, best-effort index of public Iranian chemical supplier catalogues with local mirroring, validation, exports, and coverage checks for academic procurement research.

This skill is for research and development only.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research users use this skill to install, operate, query, and audit a best-effort chemical supplier catalogue database. It guides agents to check coverage, supplier scope, molecule verification, export manifests, and crawl status before presenting results.

### Deployment Geography for Use:

Global; data scope is limited to configured public Iranian supplier catalogues.

## Known Risks and Mitigations:

Risk: Persistent crawlers and background network activity may access configured public supplier sites for long-running mirrors or resyncs.

Mitigation: Install in an isolated environment only where the operator is authorized to crawl the listed sites, and review config.yaml before enabling crawls.

Risk: Third-party geo-block bypass/archive relays or optional AI providers may send crawled source data outside the local environment.

Mitigation: Disable third-party relays, SPN2, and AI provider keys when source data is sensitive or external egress is not approved.

Risk: Shipped seed exports and catalogue rows may be incomplete, stale, or inconsistent with the claimed scope.

Mitigation: Treat seed exports as untrusted research data until independently audited, and verify coverage, supplier admission, molecule identity, and export manifests before relying on results.

Risk: Public API, dashboard, and nginx ports may expose local services if deployed without access controls.

Mitigation: Run on a trusted network and add authentication or network controls before production exposure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [README](README.md)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Deployment Guide](docs/deployment_guide.md)
- [Adding Suppliers](docs/adding_suppliers.md)
- [HTTrack Integration Guide](docs/httrack_integration.md)
- [CHANGELOG](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown guidance with inline shell commands, API query examples, and coverage or export interpretation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state crawl completeness, supplier scope, verification status, and export manifest row counts when reporting molecule or supplier results.]

## Skill Version(s):

2.18.3 (source: ClawHub release evidence, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
