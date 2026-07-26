## Description: <br>
Zero-exposure cross-device script authorization using MGC Blackbox seal functionality, where scripts are encrypted with a target node's public key, transferred as ciphertext, and decrypted only during execution on the authorized node. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zkeviny](https://clawhub.ai/user/zkeviny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security teams use this documentation skill to guide agents through sealing scripts for cross-device execution with MGC Blackbox while keeping script contents encrypted during transfer and storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill teaches users to run encrypted scripts they cannot inspect. <br>
Mitigation: Only run sealed scripts from fully trusted sources, prefer signed or hash-verified payloads, and use a constrained sandbox or least-privilege environment. <br>
Risk: Users may treat encryption as proof that a hidden script is safe. <br>
Mitigation: Review provenance and authorization separately from encryption status, and do not execute sealed payloads when the publisher or payload integrity cannot be verified. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zkeviny/skills/cross-node-script-auth) <br>
- [MGC Blackbox Repository](https://github.com/zkeviny/MGC-Blackbox) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and JSON examples and shell setup commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; it does not produce executable artifacts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
