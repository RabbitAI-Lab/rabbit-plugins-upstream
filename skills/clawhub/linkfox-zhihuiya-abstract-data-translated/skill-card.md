## Description: <br>
Retrieves translated patent titles and abstracts from the Zhihuiya (PatSnap) patent database by patent ID or publication number, with Chinese, English, and Japanese output options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to look up translated patent titles and abstracts from Zhihuiya/PatSnap when they have a patent ID or publication number. It supports single and batch lookup workflows and can optionally use a related family patent abstract when the original abstract is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent identifiers, session headers, and full lookup responses may be sent to LinkFox/PatSnap and stored locally. <br>
Mitigation: Use the skill only where third-party API disclosure and local persistence are acceptable; avoid confidential patent work unless storage is constrained and reviewed. <br>
Risk: Automatic feedback reports may be sent to LinkFox based on skill behavior or user reactions. <br>
Mitigation: Review and constrain feedback behavior before deployment where user comments, task context, or result quality notes should not be shared externally. <br>
Risk: Batch lookups consume credits dynamically and can incur higher-than-expected usage costs. <br>
Mitigation: Confirm cost-sensitive or batch requests with the user before execution and rely on the 24-hour cache for repeated identical parameters. <br>


## Reference(s): <br>
- [智慧芽摘要翻译 API 参考](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-abstract-data-translated) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown tables and JSON API responses, with full responses saved as local JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports patentId or patentNumber inputs, optional family-patent fallback, Chinese/English/Japanese target languages, 24-hour local caching, and optional inline JSON output.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
