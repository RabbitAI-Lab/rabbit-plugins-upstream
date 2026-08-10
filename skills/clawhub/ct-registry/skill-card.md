## Description:

Searches public clinical-trial registries across global and China-focused sources, normalizes heterogeneous records, and aggregates trial phase, status, sponsor, timeline, and competitor landscape outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial, medical, regulatory, and competitive-intelligence users use this skill to find comparable public trials, benchmark control designs, de-duplicate trial ideas, and export normalized registry landscapes for downstream planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public search terms may be sent to a disclosed third-party Coze endpoint during live retrieval.

Mitigation: Use only non-confidential public query terms such as drug names, diseases, sponsors, or registration numbers, and do not enter protocol, patient, sponsor-internal, or account data.

Risk: The release includes a reusable bundled endpoint token.

Mitigation: Install only if the shared-token model is acceptable for your environment; prefer CLI or environment token overrides when a separate issued token is available.

Risk: Registry search outputs can be incomplete, delayed, or unsuitable for direct regulatory use.

Mitigation: Treat outputs as planning references, keep audit metadata when needed, and verify source registry records before using results in formal submissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-registry)
- [Project homepage](https://github.com/medstatstar/ct-registry)
- [Search procedure](references/search_procedure.md)
- [CLI reference](references/cli_reference.md)
- [Search menu](references/search_menu.md)
- [Report template](references/report_template.md)
- [Language policy](references/language_policy.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [JSON, Markdown, Excel workbook, and optional PNG outputs, with conversational guidance and previewed shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live retrieval is gated by explicit run confirmation; generated reports are intended for planning and reference, not regulatory submission.]

## Skill Version(s):

0.3.79 (source: server release evidence; artifact frontmatter reports 0.3.78)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
