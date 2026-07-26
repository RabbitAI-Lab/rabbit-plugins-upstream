## Description: <br>
Extract text and layout from images and PDFs using LLMWhisperer API. Good for handwriting and complex forms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to extract layout-preserving text from PDFs and images, including handwriting and complex forms, through the LLMWhisperer API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDFs or images are sent to the external LLMWhisperer/Unstract service for processing. <br>
Mitigation: Use the skill only for documents that policy allows to be processed by that provider; avoid confidential, regulated, or highly sensitive documents unless approved. <br>
Risk: The skill requires an LLMWHISPERER_API_KEY. <br>
Mitigation: Keep the API key private and store it only in the expected environment configuration or another approved secret store. <br>


## Reference(s): <br>
- [LLMWhisperer API](https://unstract.com/llmwhisperer/) <br>
- [LLMWhisperer API endpoint](https://llmwhisperer-api.us-central.unstract.com/api/v2/whisper?mode=high_quality&output_mode=layout_preserving) <br>
- [ClawHub skill page](https://clawhub.ai/gumadeiras/skills/llmwhisperer) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Plain text output from a shell command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LLMWHISPERER_API_KEY and a user-selected PDF or image file.] <br>

## Skill Version(s): <br>
0.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
