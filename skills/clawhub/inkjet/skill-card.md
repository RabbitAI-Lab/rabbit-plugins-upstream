## Description: <br>
Print text, images, and QR codes to a wireless Bluetooth thermal printer from a MacOS device. Use `inkjet print` for output, `inkjet scan` to discover printers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaronchartier](https://clawhub.ai/user/aaronchartier) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to discover Bluetooth thermal printers and send text, Markdown, image, QR code, and local file print jobs from macOS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing and using the external `inkjet` CLI or Homebrew tap may introduce supply-chain risk. <br>
Mitigation: Verify that the pip package or Homebrew tap is trusted before installation. <br>
Risk: Printed local files, QR codes, or streamed input become physically visible. <br>
Mitigation: Review sensitive content and QR payloads before printing. <br>
Risk: Incorrect printer routing or formatting can send output to the wrong Bluetooth printer or produce unusable output. <br>
Mitigation: Check `.inkjet/config.json` or `~/.inkjet/config.json` when printer selection, margins, alignment, or font size matter. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaronchartier/skills/inkjet) <br>
- [InkJet GitHub repository](https://github.com/AaronChartier/inkjet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents toward physical printer output through the external `inkjet` CLI.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
