## Description:

Builds requirements-based open-source project shortlists using Crawlora GitHub metadata, releases, contributors, and public documentation to compare capabilities, maintenance, licenses, compatibility, and adoption questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to compare public open-source libraries and tools against requirements and produce a sourced, conditional shortlist with unresolved adoption questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project search queries, public documentation URLs, and the API key are sent to Crawlora.

Mitigation: Use the skill only when comfortable sharing these with Crawlora; keep searches bounded to public projects and exclude secrets, private repository data, and proprietary requirements from queries and scrape bodies.

Risk: Public project metadata and documentation may not establish actual compatibility, security, or license suitability.

Mitigation: Check source versions and license files, distinguish advertised from tested capabilities, and surface unanswered requirements for review.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/open-source-project-shortlisting)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown shortlist and requirements-evidence matrix]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source and version pointers, tradeoffs, and unresolved questions.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
