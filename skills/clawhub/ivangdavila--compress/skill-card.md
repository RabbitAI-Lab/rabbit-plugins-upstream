## Description:

Compress text semantically with iterative validation, anchor checksums, and verified information preservation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers, prompt engineers, and agents use this skill to reduce text size while preserving important facts through anchors, reconstruction checks, and semantic validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Semantic compression is not bit-perfect and can lose subtle or critical information, especially at L3-L4.

Mitigation: Use L1-L2 for production content, extract anchors before compression, reconstruct without access to the original, and require exact anchor matches before relying on the result.

Risk: The skill explicitly excludes medical dosages, legal text, financial figures, and safety-critical data.

Mitigation: Do not apply this skill to safety-critical or regulated text; keep the original source text instead.

Risk: The documented temporary-file validation snippet may expose confidential text if copied as written.

Mitigation: Compare sensitive validation data in memory, or use a private mktemp-created directory with restrictive permissions and cleanup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/compress)
- [Compression levels](artifact/levels.md)
- [Validation algorithm](artifact/validation.md)
- [Format-specific compression](artifact/formats.md)
- [Metrics and token budgeting](artifact/metrics.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance with compressed text examples, validation reports, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include the compression level, iteration count, anchor match rate, and confidence or validation status when compression is performed.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
