## Description: <br>
Connect ElevenLabs Agents to your OpenClaw via phone with Twilio, including caller ID authentication, voice PIN security, call screening, memory injection, and cost tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cortexuvula](https://clawhub.ai/user/cortexuvula) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to configure a phone-callable OpenClaw assistant that routes Twilio and ElevenLabs voice sessions through an LLM bridge with caller screening, memory context, and cost logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A public phone and LLM bridge can expose sensitive actions or data if reachable endpoints are weakly protected. <br>
Mitigation: Use strong random bearer tokens, restrict exposed endpoints where possible, keep caller ID and voice PIN controls enabled, and limit the tunnel to the intended bridge service. <br>
Risk: Voice calls, transcripts, memory files, and summaries can contain sensitive personal information. <br>
Mitigation: Review what call content is logged or remembered, store transcripts only when needed, protect memory files, and obtain appropriate caller consent before recording or storing call content. <br>
Risk: Inbound abuse or optional outbound calling can create unexpected phone, voice, and LLM costs. <br>
Mitigation: Use whitelist screening, rate limits, cost log monitoring, and disable outbound calling unless it is required. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cortexuvula/skills/phone-voice) <br>
- [ElevenLabs Conversational AI](https://elevenlabs.io/conversational-ai) <br>
- [Twilio](https://www.twilio.com/) <br>
- [Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline bash, JSON, and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes service setup steps, environment-variable examples, API calls, security controls, memory behavior, and cost-tracking guidance.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
