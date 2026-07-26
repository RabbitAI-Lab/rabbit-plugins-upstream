## Description: <br>
Looks up read-only Weibo creator profile details through SocialDataX, including account identifiers, biography, verification, audience counts, and other profile fields when available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve Weibo creator profile information for creator research, account basics, audience scale checks, and profile reporting. It is intended for read-only lookup workflows using a SocialDataX API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A SocialDataX API key is required in the runtime environment. <br>
Mitigation: Provide SOCIALDATAX_API_KEY only in trusted agent environments and avoid embedding API keys in skill files, prompts, or shared logs. <br>
Risk: Weibo profile IDs, profile URLs, or share text are sent to the SocialDataX service for lookup. <br>
Mitigation: Use the skill only for intended read-only profile retrieval and avoid submitting unnecessary or sensitive identifiers. <br>
Risk: API, network, parameter, or account-balance errors can interrupt profile retrieval. <br>
Mitigation: Preserve the returned error, verify the API key and lookup parameter, retry once for non-balance transient failures, and do not repeatedly retry insufficient-balance responses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-profile) <br>
- [SocialDataX API access page](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON data returned by the SocialDataX CLI or MCP tools.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY from the runtime environment and requires node and npm for the direct CLI path.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
