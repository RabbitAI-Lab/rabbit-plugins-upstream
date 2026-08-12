## Description:

Searches public clinical-trial registries across ClinicalTrials.gov, PubChem, China CDE, WHO ICTRP, EU-CTR, ChiCTR, ISRCTN, and DRKS, then normalizes and aggregates results for trial planning, de-duplication, benchmarking, and competitive landscape analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

Clinical-trial practitioners, clinicians, medical students, and analysts use this skill to search public trial registries, compare similar trials, benchmark control designs, and produce normalized landscape reports. Live retrieval should be limited to public query terms such as disease names, drug names, sponsors, or registration numbers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive search terms or competitive-intelligence queries may leave the user's environment during live retrieval.

Mitigation: Use only public, non-confidential query terms and avoid protocol, subject, CRF, or internal strategy content.

Risk: The skill uses a third-party workflow endpoint and a bundled shared bearer credential for some registry sources.

Mitigation: Review the endpoint and credential posture before installation, and override credentials through CLI or environment variables only when a trusted token is available.

Risk: Optional commercial CDE API keys and document downloads may introduce additional destination and output risk.

Mitigation: Use optional API keys and PDF downloads only after confirming the destination and intended output handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-registry)
- [Project homepage from artifact metadata](https://github.com/medstatstar/ct-registry)
- [CLI Reference](references/cli_reference.md)
- [Search Procedure](references/search_procedure.md)
- [Search Menu](references/search_menu.md)
- [SOP](references/sop.md)
- [Language Policy](references/language_policy.md)
- [Report Template](references/report_template.md)
- [Units](references/units.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with optional generated JSON, Markdown, Excel, and PNG report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Safe-preview by default; live runs can query public registries and a third-party workflow endpoint after explicit user confirmation.]

## Skill Version(s):

0.3.80 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
