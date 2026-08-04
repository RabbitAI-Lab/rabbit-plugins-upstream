## Description: <br>
Research public SEO data such as keyword volume, suggestions, related terms, difficulty, intent, organic results, and site rankings with SocQ. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External SEO practitioners, developers, and agents use this skill to collect public keyword, search result, and site-ranking data through SocQ while selecting endpoints, estimating credits, handling asynchronous tasks, pagination, and raw exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SEO queries, keywords, target domains, and filters are sent to SocQ for processing. <br>
Mitigation: Use scoped API keys and avoid confidential campaign terms unless you intend them to be processed by the external service. <br>
Risk: Requests may consume SocQ credits, especially large jobs or repeated submissions. <br>
Mitigation: Check account credits and endpoint billing before large jobs, set result limits, and inspect failed paid requests before retrying. <br>
Risk: Results may be incomplete if pagination stops early, a provider fails, a requested filter is unsupported, or an asynchronous task has not finished. <br>
Mitigation: Poll until task completion, follow every required next cursor, and report filters, collection time, partial coverage, and provider failures with the results. <br>


## Reference(s): <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [SEO Endpoint Reference](references/platform.md) <br>
- [SocQ Google Organic SERP API](https://docs.socq.ai/api-manual/seo/google-organic-serp) <br>
- [SocQ Keyword Difficulty API](https://docs.socq.ai/api-manual/seo/keyword-difficulty) <br>
- [SocQ Keyword Overview API](https://docs.socq.ai/api-manual/seo/keyword-overview) <br>
- [SocQ Keyword Search Volume API](https://docs.socq.ai/api-manual/seo/keyword-search-volume) <br>
- [SocQ Keyword Suggestions API](https://docs.socq.ai/api-manual/seo/keyword-suggestions) <br>
- [SocQ Keywords for Site API](https://docs.socq.ai/api-manual/seo/keywords-for-site) <br>
- [SocQ Ranked Keywords API](https://docs.socq.ai/api-manual/seo/ranked-keywords) <br>
- [SocQ Related Keywords API](https://docs.socq.ai/api-manual/seo/related-keywords) <br>
- [SocQ Relevant Pages API](https://docs.socq.ai/api-manual/seo/relevant-pages) <br>
- [SocQ Search Intent API](https://docs.socq.ai/api-manual/seo/search-intent) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline shell commands and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected endpoints, filters, credit estimates, task IDs, pagination cursors, result summaries, and raw JSONL retrieval steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
