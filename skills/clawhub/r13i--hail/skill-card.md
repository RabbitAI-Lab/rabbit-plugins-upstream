## Description: <br>
Send email, SMS, and voice calls from your agent. Sign up yourself with free credit, no card, and no human required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[r13i](https://clawhub.ai/user/r13i) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create a Hail workspace and send email, SMS, or voice-call communications through Hail's API. It is intended for real recipient outreach where the agent or operator has confirmed the recipient, message content, and consent basis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may contact real people through email, SMS, or voice calls. <br>
Mitigation: Require explicit operator confirmation of the recipient, channel, message content, and consent basis before each send. <br>
Risk: The HAIL_API_KEY grants access to authenticated Hail send requests. <br>
Mitigation: Store HAIL_API_KEY as a private secret and avoid exposing it in logs, prompts, chat transcripts, or generated files. <br>
Risk: Communications may contain sensitive or unauthorized information. <br>
Mitigation: Avoid sending sensitive data unless the recipient, purpose, and authorization are clearly established. <br>
Risk: Bulk or repeated sending can trigger rate limits or anti-spam enforcement. <br>
Mitigation: Respect recipient consent, avoid unsolicited bulk messages, and back off when Hail returns rate-limit responses. <br>


## Reference(s): <br>
- [Hail API Reference](https://docs.hail.so) <br>
- [Hail Pricing](https://hail.so/pricing) <br>
- [ClawHub Skill Page](https://clawhub.ai/r13i/skills/hail) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HAIL_API_KEY for authenticated send requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
