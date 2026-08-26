## Description:

dknowc trusted search helps agents retrieve authoritative Chinese policy, law, standards, and compliance materials, then deliver sourced answers with clickable provenance HTML and clean Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to answer questions about policies, regulations, standards, public services, subsidies, tax benefits, and compliance obligations with authoritative-source retrieval and clickable provenance. Agents can use it to produce a direct sourced answer, a provenance HTML report, clean Markdown, and optional policy visualization artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User queries and search context may be sent to dknowc remote services despite artifact wording that suggests questions and materials are not uploaded.

Mitigation: Treat the skill as an external search integration; use it only when the user accepts provider processing and avoid sending confidential or regulated data unless approved.

Risk: The phone verification and API-key bootstrap can expose a credential to the agent session.

Mitigation: Use managed secrets for DKNOWC_API_KEY, keep returned keys out of chat and logs, and persist credentials only after explicit user consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-trusted-search)
- [README](artifact/README.md)
- [Search introduction](artifact/reference/search_intro.md)
- [Sample search result](artifact/reference/sample_search_result.md)
- [Sample trace report](artifact/reference/sample_trace_report.html)

## Skill Output:

**Output Type(s):** [text, markdown, HTML, JSON, shell commands, configuration, guidance]

**Output Format:** [Sourced answer text plus generated HTML, clean Markdown, JSON search results, and optional self-contained visualization reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY for remote search calls; final artifacts are written under the skill's official-docs workspace.]

## Skill Version(s):

1.1.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
