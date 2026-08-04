## Description: <br>
Searches the Zhihuiya patent image database by public image URL and returns visually similar design patent records for prior-art and appearance risk review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search for design patents that look similar to a product image, then review ranked patent matches, similarity scores, patent metadata, and legal-status filters before consulting qualified patent counsel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image URLs and search parameters are sent to LinkFox/Zhihuiya for patent image search. <br>
Mitigation: Use only images and query parameters that are acceptable to share with the service provider. <br>
Risk: Local product images may be uploaded to public temporary hosting to obtain a searchable URL. <br>
Mitigation: Avoid confidential local images unless temporary public hosting is acceptable for the task. <br>
Risk: Full search responses and cache files are written locally. <br>
Mitigation: Review local LinkFox session and cache directories before sharing the workspace or artifacts. <br>
Risk: The skill may report feedback to a separate LinkFox endpoint. <br>
Mitigation: Check feedback behavior before deployment in workflows that handle sensitive user comments or proprietary context. <br>
Risk: Similarity scores can inform review but do not determine patent infringement. <br>
Mitigation: Present scores as visual similarity signals and advise users to consult a professional patent attorney for legal conclusions. <br>


## Reference(s): <br>
- [Zhihuiya Patent Image Search API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-image-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API/search results saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are saved under LinkFox session data; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.6 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
