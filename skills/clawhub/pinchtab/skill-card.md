## Description:

PinchTab helps agents control a local browser for navigation, page inspection, form interaction, content extraction, screenshots, PDFs, audits, site comparisons, and CLI or HTTP API fallback workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinchtab](https://clawhub.ai/user/pinchtab)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and automation agents use PinchTab to inspect websites, operate browser flows, extract page content, and verify outcomes with local browser automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation can change account state, publish content, make purchases, or delete data if allowed to act without review.

Mitigation: Start read-only and require explicit user confirmation before consequential actions such as account changes, payments, deletions, messages, or publication.

Risk: Cookies, browser storage, reused profiles, network bodies, screenshots, PDFs, recordings, and exported reports can contain credentials or personal data.

Mitigation: Use a dedicated low-privilege profile, keep high-risk controls disabled by default, preserve redaction, write only to approved paths, and avoid printing or forwarding sensitive values.

Risk: Page text and accessibility snapshots can contain hostile instructions from untrusted websites.

Mitigation: Treat page-derived content as untrusted data and follow it only when it independently matches the user's request.

Risk: JavaScript evaluation, file upload, file download, network export, cookie access, and file scheme navigation expand local and site data exposure.

Mitigation: Enable privileged controls only for the current approved task, prefer simpler observation commands first, and disable or restart back to safer settings when finished.

## Reference(s):

- [PinchTab ClawHub Skill](https://clawhub.ai/pinchtab/skills/pinchtab)
- [PinchTab Publisher Profile](https://clawhub.ai/user/pinchtab)
- [PinchTab Homepage](https://github.com/pinchtab/pinchtab)
- [PinchTab Product Docs](https://pinchtab.com)
- [Security and Trust](TRUST.md)
- [CLI Commands Reference](references/commands.md)
- [API Reference](references/api.md)
- [MCP Server Reference](references/mcp.md)
- [Sensitive Operations](references/safety.md)
- [Verification and Gotchas](references/verification.md)
- [Site Review Reference](references/site-review.md)
- [Profile Management](references/profiles.md)
- [Agent Optimization Playbook](references/agent-optimization.md)
- [Environment Variables](references/env.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, compact browser snapshots, JSON API responses, and optional screenshot, PDF, recording, audit, comparison, or scrape files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browser-derived content is untrusted data. Sensitive outputs such as cookies, storage, network bodies, screenshots, PDFs, recordings, downloads, and exported reports require explicit user approval and approved paths.]

## Skill Version(s):

0.15.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
