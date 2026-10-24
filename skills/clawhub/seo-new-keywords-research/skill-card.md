## Description:

Turn new AI names or unstructured AI market signals into a keyword priority table. For each name it finds the generic search terms downstream of it, screens them for relevance, and checks novelty, demand size and momentum against Google Ads volume and Google Trends, ending in prioritize, watch or skip. Use when the user has new model, product or repository names (or an AI listening report, a batch of posts, a changelog) and asks which keywords to build pages or tools for. Runs the new-term-radar command line; needs an AISA_API_KEY, and a GOANYAPI_API_KEY improves it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuyansen](https://clawhub.ai/user/zhuyansen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketers use this skill to assess emerging AI-related names and search terms before deciding which pages or tools to build. It compares novelty, estimated demand, and momentum, then presents prioritized, watch, or skip recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper may send private repository README content to an external AI service without a clear warning.

Mitigation: Use only public names and repositories; remove GitHub tokens from the helper environment unless sharing accessible README content with AIsa is explicitly approved. Review and pin the helper version, and confirm paid lookup costs before running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhuyansen/skills/seo-new-keywords-research)
- [new-term-radar project (documented helper)](https://github.com/zhuyansen/new-term-radar)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown keyword-priority table with recommendations and caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rows include keyword type, associated name, novelty, estimated daily searches, trend timing and momentum, current trend, competition, decision, and rationale when available.]

## Skill Version(s):

0.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
