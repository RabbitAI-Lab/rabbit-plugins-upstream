## Description:

Searches global clinical-trial registries, normalizes public records, and produces aggregated trial-landscape outputs for planning, de-duplication, benchmarking, and competitive intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial practitioners, clinicians, medical students, developers, and external users can use this skill to search public trial registries, compare similar trials, benchmark control designs, and build competitive trial landscapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public trial search terms to listed third-party Coze endpoints using the author's shared credential.

Mitigation: Install only when this data flow is acceptable, keep confidential patient, protocol, institutional, and proprietary strategy information out of search terms, and run live retrieval only after reviewing the outbound request.

Risk: The release ships recoverable shared Bearer tokens and pre-approves third-party outbound endpoints.

Mitigation: Treat the bundled credential as a shared endpoint credential, prefer reviewed CLI or environment overrides when needed, and rotate or stop using it if abuse is suspected.

Risk: Optional bug reports can send reviewed metadata and user-provided problem descriptions to a third-party report endpoint.

Mitigation: Review the bug-report preview before consenting and avoid including confidential data in descriptions.

Risk: PDF-download and detail-fetch requests can trigger additional retrieval from public registry sources.

Mitigation: Review each PDF-download or detail-fetch request before allowing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-registry)
- [Project homepage](https://github.com/medstatstar/ct-registry)
- [CLI reference](references/cli_reference.md)
- [Search procedure](references/search_procedure.md)
- [ClinicalTrials.gov fields](references/ctgov_fields.md)
- [Keyword matching guide](references/keyword_match.md)
- [Language policy](references/language_policy.md)
- [Standard operating procedure](references/sop.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; live runs can generate JSON, Markdown, Excel, optional PNG, and downloaded PDF files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Safe preview by default; live retrieval requires explicit user approval and sends only public search terms.]

## Skill Version(s):

0.9.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
