## Description: <br>
Encode, decode, and convert between data formats. Use when working with Base64, URL encoding, hex, Unicode, JWT tokens, hashing, checksums, or converting between serialization formats like JSON, MessagePack, and protobuf wire format. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to encode, decode, inspect, and convert data while working with API payloads, files, tokens, checksums, character encodings, and serialization formats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The quick decode script embeds input in a Python command for URL decoding, which could execute code from a crafted string. <br>
Mitigation: Do not run the quick decode script on untrusted input unless the URL-decoding step is rewritten to pass input via stdin or argv. <br>
Risk: JWTs and encoded strings may contain secrets or sensitive claims. <br>
Mitigation: Avoid pasting real tokens or secrets unless the execution environment is trusted and appropriate for that data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gitgoodordietrying/skills/encoding-formats) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires common local tools when using examples: base64, python3, openssl, or xxd.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
