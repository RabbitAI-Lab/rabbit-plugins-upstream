## Description: <br>
Searches the Zhihuiya patent database for visually similar design patents from a public image URL or an uploaded local image. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and cross-border commerce teams use this skill to compare product or design images against design patent records, review similar patent results, and identify cases that may need professional patent counsel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image URLs, uploaded local images, API credentials, and possible feedback text are sent to LinkFox services. <br>
Mitigation: Use the skill only with images and text approved for external processing, and avoid confidential or unpublished product images unless that transfer is acceptable. <br>
Risk: Local images are uploaded to obtain public URLs for patent image search. <br>
Mitigation: Prefer already public image URLs for sensitive workflows, or confirm that temporary public upload is acceptable before using a local file. <br>
Risk: Full search responses are stored locally and may include patent results and request context. <br>
Mitigation: Review the saved `linkfox/` data files and clear cached or stored results before working with sensitive matters. <br>
Risk: The search output indicates visual similarity and does not determine legal infringement. <br>
Mitigation: Treat results as triage evidence and consult a qualified patent attorney before making legal or commercial decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-image-search) <br>
- [Zhihuiya patent image search API reference](references/api.md) <br>
- [LinkFox API key guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox account and credits console](https://os.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, JSON, markdown] <br>
**Output Format:** [Markdown guidance with Python commands and JSON patent-search responses or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved locally; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
