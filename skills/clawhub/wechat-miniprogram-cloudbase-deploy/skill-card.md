## Description:

WeChat Mini Program deployment onto WeChat CloudBase: deploy cloud functions with tcb, create database collections in the console, and upload the frontend with miniprogram-ci while accounting for documented CloudBase and upload pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vincent-chao-lang](https://clawhub.ai/user/vincent-chao-lang)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to deploy WeChat Mini Programs backed by WeChat CloudBase, including cloud functions, manual collection setup, seed invocation, and frontend upload. It also helps diagnose common deployment failures such as missing collections, CloudBase namespace metadata errors, IPv6 upload whitelist rejection, and region mismatches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide deployment and upload actions that rely on private-key-based WeChat Mini Program upload authority.

Mitigation: Use only a local private key path, never paste key contents into chat, and keep upload credentials on a controlled workstation or CI runner.

Risk: The skill discusses disabling WeChat's upload IP whitelist when IPv6 egress prevents upload.

Mitigation: Prefer stable IPv4 egress or a controlled CI runner; if the whitelist must be disabled, treat it as temporary and rotate the upload key afterward.

## Reference(s):

- [WeChat CloudBase deployment pitfalls](artifact/references/pitfalls.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JavaScript examples, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local private key paths and environment variables; users should keep key contents out of chat.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
