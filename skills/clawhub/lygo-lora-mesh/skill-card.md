## Description:

LYGO LoRa mesh helps agents encode, decode, and compare compact LY1 roots_digest pulses for stock Meshtastic without driving radios, flashing firmware, or using network or subprocess behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Developers and engineers use this skill to prepare and inspect short Meshtastic text pulses for Layer D roots_digest status in off-grid or IP-down scenarios. Hardware pairing and RF transmission remain separate human actions through stock Meshtastic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake the skill for a firmware flasher or radio driver.

Mitigation: Use it only as a local encoder, decoder, and comparer; pair radios and send text through stock Meshtastic separately.

Risk: Installer or package retrieval may need reproducible supply-chain controls.

Mitigation: Avoid elevated privileges and use a pinned ClawHub installer version or verified installation path when required.

Risk: Regional LoRa frequency settings can be misapplied.

Mitigation: Confirm the local Meshtastic region before use, such as 915 MHz for CA/US nodes or 868 MHz for EU nodes, and do not mix regions.

## Reference(s):

- [ClawHub release](https://clawhub.ai/deepseekoracle/skills/lygo-lora-mesh)
- [Meshtastic documentation](https://meshtastic.org/docs/)
- [LYGO living mesh](https://clawhub.ai/deepseekoracle/skills/lygo-living-mesh)
- [Hardware reference](references/HARDWARE.md)
- [Security reference](references/SECURITY.md)
- [SkillSpector audit](references/SKILLSPECTOR_AUDIT.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include LY1 text pulses and local validation or compare results; no network, subprocess, serial, or firmware actions are required by the skill scripts.]

## Skill Version(s):

1.0.0 (source: frontmatter, claw.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
