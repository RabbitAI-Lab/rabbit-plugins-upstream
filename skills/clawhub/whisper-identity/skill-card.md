## Description: <br>
Give this agent a real, routable IPv6 (/128) identity on the Whisper network, with safe egress and externally-verifiable identity (DNSSEC + RDAP). Keyless verification needs no account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kakooch](https://clawhub.ai/user/kakooch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to assign or verify a routable Whisper IPv6 /128 identity, provide stable egress, and prove which agent made a network request. Keyless verification uses public RDAP and reverse DNS, while creating an identity requires a Whisper API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The primary setup path runs a mutable remote shell installer with broad local authority. <br>
Mitigation: Download and inspect the installer before execution, and prefer a versioned release with checksum or signature verification. <br>
Risk: Created identities and egress traffic are externally attributable to the assigned Whisper IPv6 identity. <br>
Mitigation: Use the skill only when attributable network identity is intended, and document which agent or workflow owns each issued identity. <br>
Risk: Creating identities and setting up egress requires a Whisper API key. <br>
Mitigation: Provide the key only through the WHISPER_API_KEY environment variable or an approved secret manager, and do not hard-code it in skill files, prompts, or logs. <br>


## Reference(s): <br>
- [Whisper homepage](https://whisper.online) <br>
- [Whisper documentation](https://whisper.online/docs) <br>
- [ClawHub skill page](https://clawhub.ai/kakooch/skills/whisper-identity) <br>
- [Publisher profile](https://clawhub.ai/user/kakooch) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WHISPER_API_KEY for identity creation and egress setup; keyless identity verification does not require an account.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
