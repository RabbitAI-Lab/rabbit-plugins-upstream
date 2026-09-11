## Description:

Monitor CVEs and security advisories through the Chinng AI-Agent Portal for incremental vulnerability checks, package watchlists, and actionable security summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chinng-inta](https://clawhub.ai/user/chinng-inta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to monitor watched packages, vendors, products, CVEs, and OSV identifiers through a read-only Chinng portal. It helps agents retrieve relevant advisory details, preserve attribution and source links, and separate confirmed advisory impact from inference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Watch queries sent to the external Chinng portal may reveal sensitive information about software an organization uses.

Mitigation: Review package, vendor, product, and CVE watchlists before use and avoid sending confidential or deployment-specific details unless approved.

Risk: Advisory records may include deployment-specific annotations that are not part of upstream advisory text.

Mitigation: Report only upstream advisory statements and handle non-redistributable deployment details privately with the requester.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chinng-inta/skills/security-watch)
- [Chinng portal MCP endpoint](https://portal.chinng-lab-srv.dev/mcp)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with advisory summaries, source links, and inline setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve advisory identifiers, affected-version evidence, attribution, source links, and license or reuse metadata when available.]

## Skill Version(s):

0.2.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
