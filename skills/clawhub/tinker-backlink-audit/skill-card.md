## Description:

Discovers inbound links to a domain, subdomain, or GitHub repo and classifies each source as owned, organic, or ambiguous across GitHub referrers, URL lists, backlinks.sh, and Google Search Console CSV exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and growth teams use this skill to audit inbound links, separate self-controlled links from organic backlinks, and produce reports or counts for backlink analysis workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional backlinks.sh source uses an API key, and the plaintext fallback credential file can be read by other local processes running as the same user.

Mitigation: Prefer BACKLINKS_SH_API_KEY for one-off runs or OS keychain storage; use logout to remove local storage and rotate the key server-side if exposure is suspected.

Risk: Example allowlist and history data can produce misleading owned-link counts if used unchanged for another site.

Mitigation: Replace the shipped allowlist and history series with the user's own sources before enabling --write-state or build-history.mjs --yes.

Risk: Some sources are proxies rather than raw backlink inventories, and ambiguous hostnames cannot prove ownership by domain alone.

Mitigation: Choose the source that matches the target, treat GitHub referrers as traffic data, and manually resolve ambiguous links before using them for reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/tinker-backlink-audit)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [Backlink source guide](artifact/references/sources.md)
- [Backlinks.sh API endpoint](https://api.backlinks.sh/v1/backlinks)
- [Backlinks.sh account and key management](https://backlinks.sh)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Plain text or JSON backlink audit reports with optional local state updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports owned, organic, and ambiguous link counts; write operations are opt-in through explicit flags.]

## Skill Version(s):

1.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
