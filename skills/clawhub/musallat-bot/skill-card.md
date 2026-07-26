## Description: <br>
Musallat Bot is a Gemini-powered persona bot that responds to prompts with intentionally blunt, passive-aggressive senior-developer-style commentary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[musallat-dev](https://clawhub.ai/user/musallat-dev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users can invoke the skill to generate intentionally abrasive chatbot replies for persona-based interactions or tone testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence reports an exposed apparent API key. <br>
Mitigation: Do not use the embedded key; the publisher should revoke and remove it, and users should run the skill only with their own restricted GEMINI_API_KEY. <br>
Risk: User prompts are sent to an external Gemini service with limited privacy guidance. <br>
Mitigation: Avoid sensitive prompts and use the skill only where sending content to Gemini is acceptable. <br>
Risk: The bot is designed to produce abrasive responses. <br>
Mitigation: Review generated responses before relying on them and restrict use to contexts where that persona is appropriate. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/musallat-dev/skills/musallat-bot) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/musallat-dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands] <br>
**Output Format:** [Plain text command-line response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses GEMINI_API_KEY and sends prompts to Gemini 1.5 Flash.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
