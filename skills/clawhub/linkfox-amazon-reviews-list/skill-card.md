## Description: <br>
Fetches and analyzes Amazon product reviews by ASIN across supported marketplaces, with filters for star rating, recency, helpfulness, verified purchase status, media, and keywords. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and commerce operators use this skill to retrieve Amazon customer reviews for a single ASIN, summarize customer sentiment, identify recurring complaints or praised features, and support competitor review research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retain full Amazon review responses and cache data locally. <br>
Mitigation: Review saved files before committing or sharing a workspace, and avoid using the skill where retained review data could be exposed. <br>
Risk: The skill may submit feedback automatically and includes external onboarding behavior. <br>
Mitigation: Review the feedback and onboarding behavior before use, and prefer disabling or ignoring automatic feedback submission when it is not appropriate. <br>
Risk: API calls consume LinkFox credits and repeated calls can incur additional cost. <br>
Mitigation: Confirm marketplace, ASIN, and review counts before calling the API, and reuse cached or saved results when they are sufficient. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-reviews-list) <br>
- [Amazon reviews API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown summaries with JSON API responses or saved JSON data files when the script is run.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write full review responses and cache data under a local linkfox directory; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
