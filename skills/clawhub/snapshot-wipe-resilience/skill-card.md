## Description: <br>
Detect and auto-repair partially-wiped agent workspaces, with hybrid post-quantum end-to-end encryption (X25519+ML-KEM-1024, ML-DSA-87) for any data sent off-box in sandboxes that only persist part of the filesystem between turns, and sync the recovery manifest off-box to a pastebin so it survives a total wipe. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to check whether a workspace has lost files, permissions, dependencies, models, or credentials between turns and to run tiered repair recipes for only the damaged entries. It is suited for agent sandboxes where partial filesystem persistence, size caps, or excluded build/cache directories can break later work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Restore recipes are shell commands and can modify files, credentials, dependencies, and workspace state. <br>
Mitigation: Review manifest entries before installation, sign manifests yourself, run doctor or restore with --dry-run first, and keep recipes narrowly scoped and idempotent. <br>
Risk: Pulled or mistyped manifest URLs can point to untrusted repair instructions. <br>
Mitigation: Do not run restore recipes from pulled manifests unless signatures and fingerprints verify; treat --i-trust-this-manifest as an explicit digest-bound exception. <br>
Risk: Off-box manifest sync can expose sensitive restore commands, credential placeholders, payload metadata, or operational details. <br>
Mitigation: Use encrypted sync when available, keep redaction enabled for plaintext pushes, avoid broad secrets in recipes, and treat recovery manifests as sensitive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/snapshot-wipe-resilience) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Example recovery manifest](artifact/reference/manifest.example.json) <br>
- [Turn-start repair hook](artifact/reference/turn-start-hook.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands, Python command examples, and JSON manifest configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write or update local recovery manifests, trust data, status history, escrowed small files, and paste-sync metadata when its commands are run.] <br>

## Skill Version(s): <br>
1.4.1 (source: server release evidence and skill heading) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
