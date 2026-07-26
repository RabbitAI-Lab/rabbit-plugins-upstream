## Description: <br>
AI-powered corporate portrait photo generator that accepts a personal photo and styling request, then returns a polished professional business portrait image URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wsd-mj](https://clawhub.ai/user/wsd-mj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to generate corporate portrait images from a user-provided photo, background preference, and outfit style. It is suited for office and social profile imagery when the user has the rights and consent to process the submitted photo. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow sends the selected photo and prompt to wsdsocial.com, which may expose sensitive personal imagery. <br>
Mitigation: Use only photos the user has permission to process, avoid uploading photos of other people without consent, and review the provider's privacy and retention terms for sensitive images. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wsd-mj/skills/corporate-portrait-generator) <br>
- [Server-resolved source repository](https://github.com/WSD-MJ/corporate-portrait-generator) <br>
- [WSD API key setup](https://ai.wsdsocial.com/skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with a curl example and a generated image URL response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WSD_API_KEY and sends the selected photo and styling prompt to wsdsocial.com.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
