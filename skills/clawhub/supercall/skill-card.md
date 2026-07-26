## Description: <br>
Supercall lets an OpenClaw agent make AI-powered phone calls with custom personas and goals using OpenAI Realtime API and Twilio, including automated DTMF/IVR menu navigation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xonder](https://clawhub.ai/user/xonder) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to let an agent place outbound phone calls, pursue a caller goal through a configured persona, check call status, end calls, list calls, and handle phone-tree prompts with DTMF. It is intended for workflows such as appointment confirmation, message delivery, phone-menu navigation, and autonomous voice conversations where the operator has configured the required Twilio, OpenAI, and webhook credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make autonomous real-world phone calls through a Twilio account, which may create costs and legal or consent obligations. <br>
Mitigation: Confirm call consent and applicable calling or recording rules before use, configure caller identity deliberately, and monitor Twilio usage limits and billing. <br>
Risk: Configured personas may not disclose that the caller is AI, creating disclosure, trust, or policy risk. <br>
Mitigation: Require persona and opening-line review before deployment, and add disclosure language where law, policy, or recipient expectations require it. <br>
Risk: The skill exposes public webhook or tunnel endpoints and relies on OpenAI, Twilio, tunnel, and hook secrets. <br>
Mitigation: Protect and rotate API keys and hook tokens, verify publicUrl and tunnel settings before startup, and prefer strict webhook verification where supported. <br>
Risk: Call transcripts may contain sensitive conversation content and are stored locally before being made available to the agent. <br>
Mitigation: Review, rotate, or delete stored transcripts on an appropriate retention schedule, and avoid using the skill for sensitive or safety-critical calls. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xonder/skills/supercall) <br>
- [OpenAI API Keys](https://platform.openai.com/api-keys) <br>
- [Twilio Console](https://console.twilio.com) <br>
- [ngrok Dashboard](https://dashboard.ngrok.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Configuration, Guidance] <br>
**Output Format:** [Tool results with call identifiers, call status, transcripts, and configuration-oriented text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate real outbound phone calls through Twilio, use OpenAI Realtime voice conversations, and persist call transcripts locally.] <br>

## Skill Version(s): <br>
2.0.0 (source: package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
