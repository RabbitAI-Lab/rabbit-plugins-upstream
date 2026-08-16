## Description:

Extract management guidance and forward-looking statements from SEC filings (10-K/10-Q, and 20-F/40-F/6-K for foreign private issuers). Self-contained by default (fetches from EDGAR, in-memory BM25, Claude/OpenAI). Optional heavy mode delegates to a local RAG pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinghao0724](https://clawhub.ai/user/tinghao0724)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to retrieve SEC filing passages and cited answers about management guidance, outlook, forward-looking statements, risk factors, margins, and expansion plans. It is intended to report what management stated in filings, not to provide market data, earnings-call coverage, or trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal use contacts SEC EDGAR and can be rate-limited or blocked when using a generic User-Agent.

Mitigation: Set SEC_GUIDANCE_UA to a contact-bearing User-Agent and rely on the built-in retry and backoff behavior for transient EDGAR failures.

Risk: When an Anthropic or OpenAI API key is configured, selected filing passages and the user's query may be sent to that provider for summarization.

Mitigation: Use retrieval-only mode by omitting LLM API keys when external model calls are not acceptable, or review provider handling requirements before configuring keys.

Risk: Downloaded public filing text is cached under ~/.cache/sec-guidance.

Mitigation: Clear the cache according to local retention policy if cached filing text should not persist between runs.

Risk: Unpinned Python dependencies can affect reproducibility across installations.

Mitigation: Pin dependencies or install from a lockfile when deterministic builds are required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tinghao0724/skills/sec-guidance)
- [Project homepage](https://github.com/TINGHAO0724/sec-guidance-skill)
- [SEC company tickers data](https://www.sec.gov/files/company_tickers.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown-style text with inline citations, quoted sources, filing metadata, recall stats, and optional structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Falls back to retrieval-only ranked passages when no Anthropic or OpenAI API key is configured.]

## Skill Version(s):

0.3.0 (source: SKILL.md frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
