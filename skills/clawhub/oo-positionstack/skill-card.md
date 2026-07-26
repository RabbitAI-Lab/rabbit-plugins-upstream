## Description: <br>
Positionstack helps agents operate Positionstack geocoding through an OOMOL-connected account using the oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to convert addresses or place queries into geocoding results and to resolve coordinates or IP addresses through Positionstack via an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Geocoding requests may send addresses, coordinates, or IP addresses through OOMOL and Positionstack. <br>
Mitigation: Install only when OOMOL should act as the intermediary for Positionstack geocoding, and review request payloads before execution. <br>
Risk: Actions marked as write may change Positionstack state or usage-related records. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running actions marked as write. <br>


## Reference(s): <br>
- [Positionstack homepage](https://positionstack.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the live Positionstack connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
