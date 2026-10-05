## Description:

Builds requirements-based shortlists of public open-source projects using Crawlora GitHub metadata and public project documentation to compare capabilities, maintenance, licenses, and compatibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to shortlist public open-source tools against stated requirements, compare cited project evidence, and identify adoption questions for further evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project queries, selected public documentation URLs, and the API key are sent to Crawlora.

Mitigation: Use only public project sources and a key scoped to Crawlora; install only if this disclosure is acceptable.

Risk: Broad research requests may consume more Crawlora API credits than intended.

Mitigation: Agree on shortlist scope and bound API calls and pages to the available credit budget.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/open-source-project-shortlisting)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown shortlist and requirements-evidence matrix]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes project source and version pointers, practical tradeoffs, and unresolved adoption questions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
