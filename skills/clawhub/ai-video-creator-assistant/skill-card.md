## Description: <br>
A paid AI-assisted short-video creation skill that guides users through topic, aspect-ratio, duration, and video-generation steps using the user's own Kling or Doubao API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to step through paid, guided short-video creation after selecting a topic, aspect ratio, and duration. The skill checks payment state, then guides use of the user's own video-generation platform API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment order details may be written locally without encryption if encryption configuration is missing or fails. <br>
Mitigation: Configure CLAWTIP_PAY_TO and a valid CLAWTIP_SM4_KEY before use, and delete old local order files after payment processing. <br>
Risk: The skill uses a paid clawtip flow and writes local order files. <br>
Mitigation: Proceed only after explicit user confirmation and review the payment workflow before running it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/ai-video-creator-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/jinyu12166) <br>
- [Kling AI](https://klingai.com) <br>
- [Volcengine Doubao](https://www.volcengine.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets and payment-status text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local order metadata files for the paid clawtip workflow and conversational guidance for video creation.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
