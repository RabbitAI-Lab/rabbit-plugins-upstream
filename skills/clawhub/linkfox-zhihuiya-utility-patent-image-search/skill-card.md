## Description: <br>
Searches the Zhihuiya patent database by public image URL to find visually similar utility model patents and support patent-risk review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and patent-review agents use this skill to search for utility model patents that visually resemble a product image, then review similarity scores, patent metadata, and images before deciding whether specialist legal review is needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send product images, search parameters, and feedback to LinkFox or Zhihuiya services. <br>
Mitigation: Use only images and search terms that are acceptable to share with those services, and avoid confidential local product images unless public upload is acceptable. <br>
Risk: Searches consume paid credits and repeated calls may increase cost. <br>
Mitigation: Confirm paid searches before running them and rely on the skill's cache or saved results instead of repeating equivalent requests. <br>
Risk: The security review flags high-impact upload, persistence, feedback, and installation behaviors for review before use. <br>
Mitigation: Review the skill before installing, inspect saved outputs, and make a separate trust decision before installing any onboarding package. <br>


## Reference(s): <br>
- [Zhihuiya Patent Image Search API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-utility-patent-image-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON request examples, shell commands, and saved JSON search results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results are sorted by visual similarity score when available; large API responses are saved to local JSON files and summarized in stdout.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
