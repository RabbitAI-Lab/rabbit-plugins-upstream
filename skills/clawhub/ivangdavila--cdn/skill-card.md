## Description:

Configure, optimize, and troubleshoot CDN deployments with caching strategies, security hardening, and multi-provider management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and site reliability engineers use this skill to choose CDN providers, configure caching and invalidation, harden CDN deployments, and troubleshoot cache, origin, TLS, and performance issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copy-ready purge commands can clear broad CDN caches and increase origin load.

Mitigation: Prefer targeted invalidation, test in staging, confirm provider identifiers, monitor origin capacity, and prepare rollback before production execution.

Risk: Firewall examples may block legitimate traffic if copied without current provider IP ranges and a recovery path.

Mitigation: Verify current CDN IP ranges from the provider, apply changes incrementally, keep administrative access outside the rule path, and document rollback steps.

## Reference(s):

- [CDN Skill Page](https://clawhub.ai/ivangdavila/skills/cdn)
- [Publisher Profile](https://clawhub.ai/user/ivangdavila)
- [Cloudflare IP Ranges](https://www.cloudflare.com/ips/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; users must validate provider IDs, current CDN IP ranges, origin capacity, staging behavior, monitoring, and rollback steps before production use.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
