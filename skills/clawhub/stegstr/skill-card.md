## Description: <br>
Stegstr helps agents decode, detect, embed, and post Stegstr payloads in PNG images for steganographic Nostr workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brunkstr](https://clawhub.ai/user/brunkstr) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, engineers, and agents use this skill to extract hidden payloads from PNG files, create encrypted or raw Stegstr payload images, and build Nostr note bundles for image-based sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the CLI builds from an unpinned GitHub source and its Rust dependency graph. <br>
Mitigation: Install only after trusting the Stegstr GitHub project; in sensitive environments, review or pin a known commit or release before building. <br>
Risk: Nostr private keys can be exposed if pasted into agent chats or shell commands that may be logged. <br>
Mitigation: Avoid sharing real Nostr private keys with agents or command histories; use safer key handling outside logged chat and shell contexts. <br>
Risk: Stegstr payloads are PNG-specific and can be corrupted by JPEG or other lossy image formats. <br>
Mitigation: Use lossless PNG inputs and outputs for embed, decode, and detect workflows. <br>


## Reference(s): <br>
- [Stegstr homepage](https://stegstr.com) <br>
- [Stegstr for agents](https://www.stegstr.com/wiki/for-agents.html) <br>
- [Stegstr GitHub repository](https://github.com/brunkstr/Stegstr) <br>
- [Stegstr CLI documentation](https://www.stegstr.com/wiki/cli.html) <br>
- [Stegstr bundle schema](https://raw.githubusercontent.com/brunkstr/Stegstr/main/schema/bundle.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline shell commands and CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces CLI-oriented instructions for PNG-only Stegstr workflows; decode and detect commands may emit text, base64 payloads, or Nostr bundle JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
