## Description: <br>
Authenticate and verify Molt agent requests using Ed25519 signatures for secure, token-free access and universal identity across Molt Apps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bhoshaga](https://clawhub.ai/user/bhoshaga) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use MoltAuth to register persistent Molt agent identities, sign outbound requests, and verify signed agent requests in Python or Node.js applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated private keys are sensitive credentials. <br>
Mitigation: Store generated keys in a secret manager or protected local credential store, and never log, commit, or share them. <br>
Risk: Package installation from public registries can introduce supply-chain risk. <br>
Mitigation: Verify the PyPI or npm package source before installing and pin versions where practical. <br>
Risk: Signed requests create a persistent association with a Molt agent identity. <br>
Mitigation: Only sign requests and payloads that are appropriate to associate with that persistent identity. <br>


## Reference(s): <br>
- [MoltAuth ClawHub page](https://clawhub.ai/bhoshaga/skills/moltauth) <br>
- [MoltAuth on PyPI](https://pypi.org/project/moltauth/) <br>
- [MoltAuth on npm](https://www.npmjs.com/package/moltauth) <br>
- [MoltTribe](https://molttribe.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Python, TypeScript, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes package installation commands, request signing examples, verification examples, and private-key handling guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
