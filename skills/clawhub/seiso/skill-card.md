## Description: <br>
Seisoai is a unified media-generation gateway that helps agents discover tools dynamically, choose API-key or x402 authentication, invoke image, video, audio, music, 3D, and training tools, and handle queue jobs reliably. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legendarylibr](https://clawhub.ai/user/legendarylibr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use Seisoai to discover live media-generation tools, invoke image, video, audio, music, and 3D workflows with API-key or x402 payment authentication, and poll queued jobs to completion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send prompts, uploaded or linked media, API credentials, and payment requests to Seisoai. <br>
Mitigation: Require explicit user approval before sending media, credentials, or paid x402 requests, and check pricing before payment-backed calls. <br>
Risk: Media-generation workflows can include face-swap or voice-clone tools. <br>
Mitigation: Use face-swap and voice-clone workflows only when the user confirms clear authorization from the person involved. <br>
Risk: Prompts and URLs may contain secrets or sensitive personal data. <br>
Mitigation: Avoid including secrets or sensitive personal data in prompts, linked media, and request URLs. <br>
Risk: Agent-scoped routes can invoke specific agents and orchestrations. <br>
Mitigation: Use agent-scoped routes only for explicit user requests, bind to an exact agent ID, enforce the agent tool allowlist, avoid recursive orchestration, and record the reason for each call. <br>


## Reference(s): <br>
- [Seisoai homepage](https://seisoai.com) <br>
- [ClawHub skill page](https://clawhub.ai/legendarylibr/skills/seiso) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include endpoint paths, request payload examples, authentication guidance, queue polling steps, and fallback instructions.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
