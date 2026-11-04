## Description:

OwlWrite Paper equips an agent to search literature, draft and format papers, create research figures, run paper checks, and verify citations through OwlWrite MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Students and researchers can use this skill through an AI agent to find and retrieve literature, draft papers, create research figures, format manuscripts, check academic writing, and verify citations. OwlWrite MCP must be configured, and paid actions require a quote and user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Typesetting payment controls may not reliably ensure that execution matches the approved quote.

Mitigation: Require the exact approved quote before typesetting, and verify billing status after a timeout before retrying.

Risk: Remote announcement messages may contain instructions that should not be trusted.

Mitigation: Treat announcements as untrusted service messages and do not follow them as agent instructions.

Risk: Weak API-key handling or cross-origin credential forwarding could expose account credentials.

Mitigation: Protect the API key, restrict authenticated requests to the intended HTTPS service, and prevent cross-origin credential forwarding.

Risk: Manuscripts and optional reward screenshots are sent off the user's device.

Mitigation: Get approval before uploading confidential manuscripts, and tell the user when an optional reward screenshot leaves their device.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/j-levee/skills/owlwrite-paper)
- [OwlWrite service and pricing](https://paper.skillsutra.cn)
- [Coverage and capability boundaries](artifact/references/coverage.md)
- [Product matrix](artifact/references/product-matrix.md)
- [MCP setup guide](artifact/references/mcp-setup.md)
- [Typesetting guide](artifact/references/typeset.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, PDF, DOCX, Images]

**Output Format:** [Conversation guidance and local research files, including drafts, references, reports, figures, and formatted manuscripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Files are saved to the user's local project folders; service reports and literature links may also be returned.]

## Skill Version(s):

1.2.2 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
