## Description:

An OwlWrite workbench that helps agents search literature, draft and typeset papers, create research figures, run document and citation checks, and save results locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and students use the skill to find literature, prepare and format manuscripts, create figures, and run similarity, AI-content, citation, and document checks through an OwlWrite-enabled agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Typesetting charges may not be bound to the quote the user approved.

Mitigation: Confirm the run executes the exact approved quote; after errors, check task and billing status before retrying.

Risk: Manuscripts and screenshots may be processed in the cloud before payment is confirmed, and backend retention assurances are unverified.

Mitigation: Get deliberate approval before uploads, especially for unpublished research, and avoid promising retention or deletion terms.

Risk: Credentials could be exposed through unsafe redirects or an unintended API destination.

Mitigation: Keep the API destination fixed to https://owl.skillsutra.cn and require credential-safe redirects.

Risk: Unreviewed dependency changes may affect the local Python client environment.

Mitigation: Use an isolated Python environment with reviewed dependency versions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/j-levee/skills/owlwrite-paper)
- [OwlWrite service website](https://paper.skillsutra.cn)
- [Product matrix](artifact/references/product-matrix.md)
- [Typesetting guide](artifact/references/typeset.md)
- [Coverage guide](artifact/references/coverage.md)
- [MCP setup guide](artifact/references/mcp-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, PDF and Word documents, Research figures, Reports, CSV and JSON files]

**Output Format:** [Conversational responses and locally saved documents, figures, and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available file formats depend on the task.]

## Skill Version(s):

1.1.9 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
