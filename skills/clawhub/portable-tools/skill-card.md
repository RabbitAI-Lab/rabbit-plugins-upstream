## Description: <br>
Build cross-device tools without hardcoding paths or account names. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tunaissacoding](https://clawhub.ai/user/tunaissacoding) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to design scripts and tools that adapt to different file paths, account names, data formats, and local environments. It provides portability patterns, debugging checks, and a pre-publish checklist for tools intended to run across multiple machines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Debugging examples may lead users to expose real OAuth, keychain, token, or credential JSON values. <br>
Mitigation: Use redacted prefixes or suffixes, lengths, hashes, field-presence checks, and expiry timestamps instead of pasting, printing, screenshotting, or logging real secrets. <br>


## Reference(s): <br>
- [Portable Tools README](README.md) <br>
- [Portable Tools Methodology](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, code] <br>
**Output Format:** [Markdown with inline shell and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a bash pre-publish checklist for scanning portability issues.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
