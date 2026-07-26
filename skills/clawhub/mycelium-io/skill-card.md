## Description: <br>
Use the mycelium CLI to join coordination rooms, negotiate with other agents via CognitiveEngine, and share persistent memory across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juliarvalenti](https://clawhub.ai/user/juliarvalenti) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to coordinate multiple AI agents in Mycelium rooms, run structured negotiations, and persist shared markdown memories and plans across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Room memories are persistent shared plaintext data and may sync to the configured server. <br>
Mitigation: Do not store secrets, credentials, personal information, or sensitive private context in room memories; use a trusted, access-controlled backend. <br>
Risk: The skill directs agents to use an installed Mycelium CLI and a third-party Homebrew tap. <br>
Mitigation: Install only after reviewing and trusting the CLI source, tap, and release artifacts; allowlist the binary only for agents intended to use Mycelium. <br>
Risk: Weakly supported negotiation outcomes can still become shared plans if agents accept without genuine agreement. <br>
Mitigation: Check negotiation status and contested indicators before acting on decisions with low provenance weight or high social compliance. <br>


## Reference(s): <br>
- [Mycelium project homepage](https://github.com/mycelium-io/mycelium) <br>
- [Mycelium Homebrew tap](https://github.com/mycelium-io/homebrew-tap) <br>
- [Mycelium 2.0.0 release notes](https://github.com/mycelium-io/mycelium/releases/tag/v2.0.0) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance is intended for agents operating an installed mycelium CLI against a configured room backend.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
