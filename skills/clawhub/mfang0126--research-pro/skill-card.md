## Description:

Research Pro helps agents conduct systematic multi-source research by breaking questions into sub-questions, iterating searches, tracking evidence, and producing structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mfang0126](https://clawhub.ai/user/mfang0126)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users use this skill to conduct scoped external research, compare options, and produce evidence-linked reports with conclusions, source lists, disagreements, and open gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants and reuses credentials for external research services.

Mitigation: Use dedicated low-privilege API keys, keep keys outside the skill tree, and disable host credential reuse with RESEARCH_PRO_TRUST_HOST_ENV=0 in sensitive workspaces.

Risk: External calls and research traces can expose confidential topics or retained research details.

Mitigation: Review trace settings before use and turn tracing off for confidential work with RESEARCH_PRO_TRACE=off.

Risk: One-shot setup and credential wrappers can modify agent environments or inject credentials into commands.

Mitigation: Run setup or run-with-creds only after reviewing the command target and only for commands explicitly chosen by the user.

Risk: Session cookies such as Reddit credentials can increase account exposure if reused by an agent process.

Mitigation: Avoid REDDIT_SESSION or TOKEN_V2 cookies and prefer scoped API keys where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mfang0126/skills/research-pro)
- [README](README.md)
- [Setup Guide](SETUP.md)
- [Security Notes](references/security.md)
- [Runtime Notes](references/runtimes.md)
- [Research Quality Checklist](references/research-quality-checklist.md)
- [Evidence-Linked Research Baseline](references/evidence-linked-research-baseline-2026-07-27.md)
- [Research Evidence Core v4 Draft Spec](references/research-evidence-core-v4-draft-spec.md)
- [Research Pro v3 Implementation Gap Audit](references/research-pro-v3-implementation-gap-audit-2026-07-27.md)
- [Tavily Search API Reference](references/tavily/search.md)
- [Tavily Extract API Reference](references/tavily/extract.md)
- [Tavily Research API Reference](references/tavily/research.md)
- [xAI Tools Docs Quick Links](references/xai/xai-tools-links.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown structured research reports with citations, tables, source lists, and occasional inline shell commands or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include YAML frontmatter, comparison matrices, disagreement summaries, unresolved gaps, and trace or setup guidance.]

## Skill Version(s):

3.17.2 (source: server release metadata; artifact frontmatter reports 3.17.1-mf)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
