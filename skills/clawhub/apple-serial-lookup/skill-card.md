## Description: <br>
Apple Serial Lookup helps identify Apple devices from serial numbers, including iPhones, iPads, Macs, Apple Watch, Apple TV, and iPods, using local decoding plus guided web lookups for specs, manufacturing details, warranty status, and model information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[siatrial](https://clawhub.ai/user/siatrial) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and support staff use this skill to identify Apple devices from serial numbers, locally decode older serials, and decide when to use Apple or third-party lookup pages for complete specs or coverage details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Apple serial numbers can be sensitive asset identifiers when sent to external lookup or search services. <br>
Mitigation: Prefer the local decoder for older serials and use web lookups only when the user accepts sharing the serial with external services. <br>
Risk: New randomized Apple serials and incomplete model-code mappings can limit local identification accuracy. <br>
Mitigation: Treat local results as partial when the format is randomized or the model code is unknown, and direct users to Apple Check Coverage or other documented lookup sources for confirmation. <br>


## Reference(s): <br>
- [Apple Serial Lookup on ClawHub](https://clawhub.ai/siatrial/skills/apple-serial-lookup) <br>
- [Serial Format and Encoding](references/serial-format.md) <br>
- [Model Code Database](references/model-codes.md) <br>
- [EveryMac Ultimate Mac Lookup](https://everymac.com/ultimate-mac-lookup/?search_keywords=SERIAL) <br>
- [Apple Check Coverage](https://checkcoverage.apple.com/) <br>
- [Beetstech Apple Device Lookup](https://beetstech.com/apple-device-lookup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown summary with optional JSON from the bundled decoder script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local decode fields such as manufacturing location/date, model codes, basic specs, and links for external lookup when needed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
