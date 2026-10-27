## Description:

Turn new AI names or unstructured AI market signals into a keyword priority table. For each name it finds the generic search terms downstream of it, screens them for relevance, and checks novelty, demand size and momentum against Google Ads volume and DataForSEO Trends (an estimate of Google search interest), ending in prioritize, watch or skip. Use when the user has new model, product or repository names (or an AI listening report, a batch of posts, a changelog) and asks which keywords to build pages or tools for. Runs the new-term-radar command line; needs an AISA_API_KEY, and a GOANYAPI_API_KEY improves it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuyansen](https://clawhub.ai/user/zhuyansen)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners and product teams use the skill to turn new AI model, product, repository, or market-signal inputs into a prioritized keyword table for deciding which pages or tools to build.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyword lookups use external services and may incur paid charges.

Mitigation: Use public names and identifiers only, and review the selected names and estimated charge before approving a run.

Risk: The pinned third-party runtime was not independently verified.

Mitigation: Review the pinned package before execution and keep it isolated from unrelated credentials and data.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zhuyansen/skills/seo-new-keywords-research)
- [Example configuration](https://github.com/zhuyansen/new-term-radar/blob/v0.6.0/config.example.json)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keyword rows with prioritize, watch, or skip decisions and estimated demand and momentum signals.]

## Skill Version(s):

0.6.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
