## Description:

Helps agents find, verify, and format academic references using Phở Research Tools, while flagging incorrect, fabricated, or retracted citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thaohienhomes](https://clawhub.ai/user/thaohienhomes)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and reviewers use this skill to check academic references, correct citation details, and produce bibliographies with clearly reported verification status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference text and citation queries may be sent to an external verification service, potentially exposing confidential manuscript content.

Mitigation: Avoid checking confidential manuscripts unless external processing is acceptable; share only the references needed for verification.

Risk: A citation may be unverified, incorrectly matched, or retracted despite appearing plausible.

Mitigation: Check verification status and corrected metadata before citing; disclose unresolved results and do not silently use retracted references.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thaohienhomes/skills/pho-citation-check)
- [Phở Research Tools MCP server](https://mcp.pho.chat/mcp)
- [Phở citation checker](https://pho.chat/tools/citation-checker/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with citations, bibliographies, and verification summaries; optionally BibTeX, RIS, or CSL-JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports verified, corrected, unverified, fabricated, and retracted references; can provide PRISMA flow diagrams.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
