## Description:

Checks long .docx, Markdown, and text documents for internal consistency issues such as broken cross-references, numbering gaps, TOC mismatches, terminology drift, placeholders, stale years, and merge-loss evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, editors, proposal teams, publishers, and technical writers use this skill to run repeatable offline checks before accepting or releasing long documents. It is suited for cross-reference audits, numbering audits, terminology consistency checks, TOC reconciliation, stale placeholder detection, and merge-loss review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local documents and optional baseline or glossary files that may contain confidential material.

Mitigation: Run it locally and offline, and review any separate U-King setup or human-service workflow before sending documents externally.

Risk: The checker verifies internal consistency, not factual correctness, legal sufficiency, technical correctness, or acceptance by a reviewer.

Mitigation: Use the findings as an editorial QA aid and keep human review for factual, legal, technical, and acceptance decisions.

Risk: Word auto-numbering and auto-captions can be stored as fields outside the body text the tool reads.

Mitigation: Treat any note about unreadable fields as an untested area and manually inspect those captions or numbering sequences.

Risk: Generated reports include attribution and contact footer text.

Mitigation: Review distribution requirements and preserve or handle attribution consistently with the applicable license and notices.

## Reference(s):

- [README](README.md)
- [Services and Human Review Scope](SERVICES.md)
- [U-King](https://u-king.org)
- [ClawHub Skill Listing](https://clawhub.ai/dongsheng123132/skills/doc-consistency)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown report or JSON findings list with re-check shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are located by paragraph or line; JSON mode is untruncated; the default report lists the first 20 findings unless configured otherwise.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
