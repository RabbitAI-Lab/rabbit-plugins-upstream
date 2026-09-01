## Description:

Searches academic literature via arXiv, Semantic Scholar, and open-access PDFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agents use this skill to find academic papers, build literature reviews or citation chains, and extract useful information from open-access PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic requests mentioning papers or PDFs may invoke the skill when the user did not intend to run academic search or PDF summarization.

Mitigation: Confirm the user's intent before searching or converting documents when the request is ambiguous.

Risk: Using the skill can send paper URLs, metadata queries, or PDF content to external academic search and conversion services.

Mitigation: Avoid sending private, sensitive, or unpublished documents unless the user has approved the external service use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-tome-papers)
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/tome)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with paper metadata, summaries, citation details, extraction notes, and fallback guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to academic sources and notes about PDF conversion or unavailable open-access copies.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
