## Description: <br>
Searches the Zhihuiya patent database by image URL to find visually similar utility model patents for patent risk review and prior-art research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and patent-review workflows use this skill to submit a public image URL or uploaded product image, search for similar utility model patents, and review ranked patent matches. It is not a substitute for legal advice or a freedom-to-operate opinion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends product image URLs, search filters, API credentials, and session metadata to LinkFox/Zhihuiya services. <br>
Mitigation: Use it only when that external processing is acceptable, avoid confidential product images in sensitive workflows, and keep API credentials scoped and protected. <br>
Risk: Local images may be uploaded to a public URL that remains valid for 24 hours. <br>
Mitigation: Prefer already public images when possible, obtain explicit approval before uploading local images, and avoid uploading confidential files. <br>
Risk: Local cache and session files may contain sensitive search material. <br>
Mitigation: Periodically delete the local linkfox cache and session data after searches involving sensitive products or patent investigations. <br>
Risk: Automatic feedback reporting is identified by the server security summary as lacking clear user consent controls. <br>
Mitigation: Review or disable feedback reporting before using the skill in sensitive workflows. <br>


## Reference(s): <br>
- [API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-utility-patent-image-search) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Files, Markdown] <br>
**Output Format:** [Markdown guidance with shell commands and JSON patent-search responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved under linkfox session data; small responses print full JSON to stdout, while large responses print a summary unless --inline is used.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
