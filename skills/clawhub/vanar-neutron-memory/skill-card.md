## Description: <br>
Save and recall agent memory with semantic search. Context that persists across every session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[naeemmaliki036](https://clawhub.ai/user/naeemmaliki036) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to save text memories, run semantic memory search, and optionally recall or capture conversation context through opt-in hooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved memories, search queries, and enabled auto-captured conversation turns are sent to a hosted Vanar Neutron service. <br>
Mitigation: Keep auto-capture and auto-recall disabled unless remote retention is acceptable, and avoid saving secrets, regulated data, or confidential business material. <br>
Risk: The skill requires an API key for the hosted memory service. <br>
Mitigation: Prefer an environment variable or tightly permissioned credentials file, and rotate the key if it is exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/naeemmaliki036/skills/vanar-neutron-memory) <br>
- [Vanar Neutron dashboard and API keys](https://openclaw.vanarchain.com/) <br>
- [Vanar Neutron signup](https://openclaw.vanarchain.com/signup) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Shell command output and JSON API responses, with Markdown setup guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, network access to the hosted Neutron API, and an API key supplied through the environment or credentials file.] <br>

## Skill Version(s): <br>
1.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
