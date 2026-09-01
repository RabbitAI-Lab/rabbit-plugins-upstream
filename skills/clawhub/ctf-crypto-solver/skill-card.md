## Description:

Helps agents identify and solve CTF cryptography challenges involving RSA, AES, ECC, lattices, PRNGs, hashes, and signature attacks.

This skill is for research and development only.

## Publisher:

[yxy050208](https://clawhub.ai/user/yxy050208)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security learners, and CTF practitioners use this skill to triage cryptography challenges, select likely attack paths, and draft solver scripts or shell commands for authorized CTF, lab, or defensive research work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes runnable exploit and credential-recovery playbooks that could be misapplied outside authorized CTF, lab, or defensive research contexts.

Mitigation: Use it only for authorized CTF, lab, or defensive research work, and keep it out of general browsing or real-service workflows.

Risk: Generated scripts or commands may handle sensitive material such as wallets, accounts, cookies, private keys, or third-party systems.

Mitigation: Do not use the skill with real wallets, accounts, cookies, private keys, production secrets, or systems you are not authorized to test.

Risk: Generated cryptography attack scripts may behave incorrectly or cause unintended effects when run against a network target.

Mitigation: Review generated scripts before execution and run them only against controlled or explicitly authorized targets.

## Reference(s):

- [CTF Cryptography Reference Index](references/ctf-crypto/SKILL.md)
- [Advanced Mathematical Attacks](references/ctf-crypto/advanced-math.md)
- [Classic Ciphers](references/ctf-crypto/classic-ciphers.md)
- [Elliptic Curve Attacks](references/ctf-crypto/ecc-attacks.md)
- [Exotic Algebraic Structures](references/ctf-crypto/exotic-crypto.md)
- [Exotic Algebraic Structures Part 2](references/ctf-crypto/exotic-crypto-2.md)
- [Historical Ciphers](references/ctf-crypto/historical.md)
- [Lattice and LWE Attacks](references/ctf-crypto/lattice-and-lwe.md)
- [Modern Cipher Attacks](references/ctf-crypto/modern-ciphers.md)
- [Modern Cipher Attacks Continued](references/ctf-crypto/modern-ciphers-2.md)
- [Modern Cipher Attacks Part 3](references/ctf-crypto/modern-ciphers-3.md)
- [PRNG and Key Recovery](references/ctf-crypto/prng.md)
- [PRNG Attacks](references/ctf-crypto/prng-attacks.md)
- [RSA Attacks](references/ctf-crypto/rsa-attacks.md)
- [RSA Attacks Part 2](references/ctf-crypto/rsa-attacks-2.md)
- [Stream Cipher Attacks](references/ctf-crypto/stream-ciphers.md)
- [ZKP, Solvers, and Advanced Techniques](references/ctf-crypto/zkp-and-advanced.md)
- [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce solver scripts, attack selection guidance, dependency installation commands, and environment setup instructions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
