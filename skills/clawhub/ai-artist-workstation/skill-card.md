## Description: <br>
Ai Artist Workstation helps commercial artists and designers route AI image requests through portrait or text-to-image workflows, review prompts, and prepare customer delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External commercial artists and designers use this skill to accept AI image orders, choose a generation route, handle prompt review, and prepare image delivery. It is most relevant for avatar, product-image, style-image, and AI portrait workflows where customer images and delivery links are handled with consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may handle customer photos, cloud links, and e-commerce delivery actions. <br>
Mitigation: Use only non-sensitive customer images or images covered by explicit consent, and require user confirmation before uploads, share-link creation, or customer messages. <br>
Risk: The skill requests command execution and API-key-backed image services. <br>
Mitigation: Review proposed commands before execution, keep API keys in scoped environment variables, and prevent keys from appearing in logs, errors, or generated output. <br>
Risk: Generated portraits or commercial image deliverables may be incorrect, misleading, or unsuitable for the order. <br>
Mitigation: Review generated images and delivery text before sending them to customers, especially when face preservation, commercial use, or refunds are involved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-artist-workstation) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference generated image URLs, local image paths, and cloud delivery links when connected image services are used.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
