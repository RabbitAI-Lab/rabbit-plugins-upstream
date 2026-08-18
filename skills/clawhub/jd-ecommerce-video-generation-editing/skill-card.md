## Description:

Generates and edits JD e-commerce product-page and ad videos for 3C electronics and appliances using AI Hive text-to-video, image-to-video, reference, edit, and extend workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce merchants, operators, and content teams use this skill to create, revise, and extend product demonstration videos for JD product pages, JD ads, installation walkthroughs, interface explanations, compatibility evidence, and supplier-video cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and media are sent to AI Hive for generation and may include private product information.

Mitigation: Use only assets intended for upload, verify the configured AI Hive base URL before running, and avoid confidential files unless sharing them with the service is approved.

Risk: The skill can save an AI Hive API key in a local home-directory config file.

Mitigation: Use a dedicated API key, keep the config file permissions restricted, and rotate or revoke the key when it is no longer needed.

Risk: Generated videos can misstate product parameters, compatibility, certifications, warranties, or platform compliance if source facts are incomplete.

Mitigation: Base prompts on merchant-provided facts and visible evidence, then manually review technical claims and current JD category, product-page, and advertising rules before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/jd-ecommerce-video-generation-editing)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Files, Markdown guidance]

**Output Format:** [Markdown guidance with bash commands, JSON task responses, and downloaded media files from the AI Hive CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can upload selected media, submit generation tasks, poll task status, and optionally save generated video or image outputs to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
