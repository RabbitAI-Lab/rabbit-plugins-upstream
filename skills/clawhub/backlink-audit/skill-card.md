## Description:

Discovers inbound links to a domain, subdomain, or GitHub repo and classifies each source as controlled, organic, or ambiguous.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and growth teams use this skill to audit backlinks, separate self-created links from organic mentions, and refresh inbound-link reporting from GitHub referrers, provided URL lists, backlinks.sh, or Google Search Console CSV exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A legacy plaintext backlinks.sh credentials file may still exist from an older version.

Mitigation: Review before installing and remove the old file or run the logout command before using the skill.

Risk: The shipped allowlist and build-history dataset are examples from the publisher, not the user's own backlink history.

Mitigation: Replace the allowlist and historical series before using write-state or running build-history with confirmation.

Risk: The backlinks source sends a user API key to backlinks.sh and may consume paid API calls.

Mitigation: Use offline sources when possible and select the backlinks source only after confirming the key and cost expectations.

## Reference(s):

- [Backlink sources](artifact/references/sources.md)
- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/backlink-audit)
- [backlinks.sh API endpoint](https://api.backlinks.sh/v1/backlinks)
- [backlinks.sh account and API service](https://backlinks.sh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May optionally write inbound-link counts to an OpenClaw state file when the user passes the write-state flag.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
