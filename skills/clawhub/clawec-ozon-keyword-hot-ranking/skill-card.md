## Description: <br>
Queries ClawEC's Ozon hot keyword ranking API for search, order, conversion, supply-demand, and competitor metrics with category and filter support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cross-border ecommerce sellers and analysts use this skill to research Ozon keyword demand, category search trends, and product-selection opportunities. It helps compare hot keywords by search index, growth, order conversion, order amount, supply-demand ratio, and competition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ClawEC API key and sends Ozon keyword query parameters to the ClawEC API. <br>
Mitigation: Confirm the data-sharing posture before use and provide the key through the CLAWEC_API_KEY environment variable instead of hardcoding it. <br>


## Reference(s): <br>
- [Response schema](artifact/references/response-schema.md) <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-ozon-keyword-hot-ranking) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with optional shell command examples and tabular keyword summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default reports are in Chinese and may include query conditions, ranked keyword tables, opportunity observations, and 3-5 recommended keywords.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
