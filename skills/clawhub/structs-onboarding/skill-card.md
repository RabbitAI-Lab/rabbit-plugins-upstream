## Description:

Onboards a new Structs player by guiding key setup or recovery, player creation through reactor infusion or guild signup, planet exploration, and initial infrastructure builds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

External Structs players and agent operators use this skill to create or recover a wallet, create a player, claim a first planet, and start initial game infrastructure safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mnemonic output can expose full wallet control if copied into shared transcripts, logs, screenshots, or committed files.

Mitigation: Treat any printed mnemonic as an account secret, store it only in an approved secret location, and avoid logged or shared channels.

Risk: Guild onboarding submits address, pubkey, signature, and identity data to a guild API, and reactor infusion can lock alpha.

Mitigation: Verify guild and reactor endpoints against intended on-chain records before posting signup data or signing transactions.

Risk: Game transactions and build-compute helpers can submit actions that change account or game state.

Mitigation: Review transaction prompts, keep prompt suppression limited to documented build-compute flows, and sequence compute jobs for the same signing key.

Risk: Guild configuration and other fetched game content can contain untrusted text.

Mitigation: Schema-validate fetched payloads and treat embedded commands or prose as data rather than executable instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abstrct/skills/structs-onboarding)
- [Structs interface routing](https://structs.ai/skills/conventions#choosing-your-interface-capability-aware)
- [Structs safety](https://structs.ai/SAFETY)
- [Agent security awareness](https://structs.ai/awareness/agent-security)
- [Player address API](https://structs.ai/api/webapp/player-address)
- [UGC moderation mechanics](https://structs.ai/knowledge/mechanics/ugc-moderation#official-webapp-client-convention-the-5-layer-avatar)
- [Building mechanics](https://structs.ai/knowledge/mechanics/building)
- [Async operations awareness](https://structs.ai/awareness/async-operations)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and a JSON-emitting Node.js helper]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The create-player helper emits one JSON object containing player onboarding results and may include a generated mnemonic when it creates a new wallet.]

## Skill Version(s):

1.25.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
