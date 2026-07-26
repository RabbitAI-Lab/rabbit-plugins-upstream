## Description: <br>
LYGO ASCII Art Studio routes photo-to-ASCII, text art, and type art requests to a live client-side web tool with no-upload handling, tuning controls, and TXT/PNG export options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to route photo-to-ASCII requests to the LYGO web studio, provide concise operating guidance, and help users copy or export text and PNG results. The skill is intended as a pointer and operator brief, not as a local image-processing pipeline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive images could be exposed if the live external page behavior differs from the no-upload claim. <br>
Mitigation: Verify the live page behavior and source before using sensitive images, and avoid entering private images unless client-side handling is confirmed. <br>
Risk: Generated art could be published to public services without user consent if an agent extends the workflow. <br>
Mitigation: Require explicit user confirmation before publishing or sharing generated art to GitHub, Hugging Face, social platforms, or other public surfaces. <br>


## Reference(s): <br>
- [Lattice registration](references/LATTICE.md) <br>
- [LYGO ASCII Art Studio](https://eternalhaven.ca/lygo-ascii-art.html) <br>
- [GitHub Pages mirror](https://deepseekoracle.github.io/eternalhaven/lygo-ascii-art.html) <br>
- [Excavationpro mirror](https://deepseekoracle.github.io/Excavationpro/lygo-ascii-art.html) <br>
- [Source repository link](https://github.com/DeepSeekOracle/eternalhaven) <br>
- [Immutable anchors ledger](https://github.com/DeepSeekOracle/lygo-protocol-stack/blob/main/docs/network_builder/IMMUTABLE_ANCHORS.json) <br>
- [ClawHub listing](https://clawhub.ai/deepseekoracle/skills/lygo-ascii-art-studio) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with canonical URLs, short user instructions, and optional shell command snippets for lattice verification.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill points users to an external browser page and does not process images locally inside the agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
