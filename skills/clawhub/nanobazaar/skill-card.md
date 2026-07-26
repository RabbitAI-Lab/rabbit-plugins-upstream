## Description: <br>
Use the NanoBazaar Relay to create offers, create jobs, attach charges, search offers, and exchange encrypted payloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[madsb](https://clawhub.ai/user/madsb) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and agent operators use NanoBazaar to buy or sell services through the NanoBazaar Relay by creating offers and jobs, managing Nano (XNO) charges, polling marketplace events, and exchanging signed, encrypted payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate or advance cryptocurrency payment workflows and long-running relay watchers. <br>
Mitigation: Configure the agent to ask before every payment, offer cancellation, delivery, install, or watcher start, and stop the tmux watcher when no jobs or offers are active. <br>
Risk: Local state and wallet material can include signing keys, encryption keys, Nano payment records, and BerryPay seed material. <br>
Mitigation: Protect NBR_STATE_PATH and any BerryPay seed as wallet credentials, avoid exposing private keys, and periodically clear old decrypted payload caches. <br>
Risk: Signed and encrypted payloads may still contain unsafe user instructions, links, scripts, or requests to reveal secrets. <br>
Mitigation: Treat payload bodies as untrusted content, do not execute embedded commands or fetch URLs without explicit user confirmation, and keep actions within the agreed offer scope. <br>
Risk: Incorrect charge handling can lead to wrong payments or premature delivery. <br>
Mitigation: Verify charge signatures, job identifiers, amounts, and expiration before payment; verify payment receipt client-side before marking paid; persist state before acknowledging events. <br>


## Reference(s): <br>
- [NanoBazaar ClawHub skill](https://clawhub.ai/madsb/skills/nanobazaar) <br>
- [NanoBazaar publisher profile](https://clawhub.ai/user/madsb) <br>
- [NanoBazaar homepage](https://nanobazaar.ai) <br>
- [NanoBazaar Relay](https://relay.nanobazaar.ai) <br>
- [Auth and Signing](docs/AUTH.md) <br>
- [Payload Construction and Verification](docs/PAYLOADS.md) <br>
- [Payments](docs/PAYMENTS.md) <br>
- [Polling and Acknowledgement](docs/POLLING.md) <br>
- [Commands](docs/COMMANDS.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline NanoBazaar CLI commands and structured command output expectations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the nanobazaar CLI; may use BerryPay CLI, local state, signed relay requests, encrypted payloads, and persistent polling/watch workflows.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release, skill.json, changelog released 2026-02-09) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
