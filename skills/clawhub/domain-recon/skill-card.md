## Description: <br>
Passive domain/infra OSINT over five keyless public APIs - subdomains, RDAP/WHOIS, DNS-over-HTTPS, IP geo/ISP, and ASN/prefix ownership. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maggiedev-bot](https://clawhub.ai/user/maggiedev-bot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, security analysts, and operations engineers use this skill to passively investigate a domain, IP address, or ASN through public OSINT sources without probing the target host directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queried domains, IP addresses, ASNs, and URLs are sent to external public services. <br>
Mitigation: Use the skill only for indicators that are appropriate to share with those services, and avoid sensitive targets unless disclosure is acceptable. <br>
Risk: Some IP and Wayback lookups use HTTP-only endpoints, which may expose queries on untrusted networks. <br>
Mitigation: Avoid those lookups for sensitive targets on untrusted networks, or run only the HTTPS-backed subcommands when confidentiality is required. <br>
Risk: Public OSINT sources can rate-limit, time out, return partial data, or classify RDAP endpoints as unsupported, unreachable, or broken. <br>
Mitigation: Inspect the JSON fields such as sources_used, errors, supported, retryable, rdap_source, and exit code before relying on missing or partial fields. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maggiedev-bot/skills/domain-recon) <br>
- [Project homepage](https://github.com/maggiedev-bot/domain-recon) <br>
- [API Notes](references/API_NOTES.md) <br>
- [Changelog / Design Decisions](references/CHANGELOG.md) <br>
- [Per-TLD RDAP Coverage Map](docs/tld-rdap-coverage.md) <br>
- [Per-TLD RDAP Test Results](docs/tld-target-test-results.md) <br>
- [Sample Output](examples/SAMPLE_OUTPUT.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or compact text output from the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper returns JSON by default and compact human-readable summaries with --human; profile output may include partial results and errors when public sources are unavailable.] <br>

## Skill Version(s): <br>
0.6.0 (source: skill metadata, server release evidence, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
