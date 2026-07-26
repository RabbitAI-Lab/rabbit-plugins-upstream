## Description: <br>
Agnes Image 2.1 Flash helps agents generate and edit high-information-density images through text-to-image, image-to-image, and multi-image workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lutongsuo](https://clawhub.ai/user/lutongsuo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative users use this skill to produce marketing visuals, concept art, product imagery, social media assets, style transfers, and multi-image compositions with the Agnes Image 2.1 Flash API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and referenced image URLs are sent to the external Agnes service for processing. <br>
Mitigation: Avoid secrets, private internal URLs, confidential images, and personal data unless that third-party processing is acceptable. <br>


## Reference(s): <br>
- [Agnes Image 2.1 Flash API](references/API.md) <br>
- [Agnes Image 2.1 Flash Prompt Guide](references/PROMPT_GUIDE.md) <br>
- [Agnes Image 2.1 Flash Examples](references/EXAMPLES.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, files, text] <br>
**Output Format:** [Markdown guidance with bash commands; generated outputs can be image URLs, PNG files, or Base64 text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ANGES_API_KEY or AGENT_ANGES_API_KEY and sends prompts plus referenced image URLs to the Agnes API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
