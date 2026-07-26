## Description: <br>
Track baby sleep, feeding, diapers, and growth via Huckleberry app API. Use for logging baby activities through natural language. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaronn](https://clawhub.ai/user/aaronn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External caregivers and agents use this skill to translate natural-language baby tracking requests into Huckleberry CLI actions for sleep, feeding, diaper, growth, and history workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Huckleberry account credentials. <br>
Mitigation: Use protected environment variables or a tightly permissioned credentials file, and do not commit credential files. <br>
Risk: The skill can read and update sensitive child activity, growth, and history records. <br>
Mitigation: Install only in trusted agent environments and verify important entries in the Huckleberry app after logging. <br>
Risk: Setup may depend on reviewing or pinning the GitHub-hosted Huckleberry API dependency. <br>
Mitigation: Pin or review the dependency before use in environments where supply-chain stability matters. <br>


## Reference(s): <br>
- [py-huckleberry-api](https://github.com/Woyken/py-huckleberry-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON] <br>
**Output Format:** [Markdown guidance with CLI commands; CLI output is plain text or JSON for supported commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require Huckleberry credentials and may read or update baby activity, growth, and history records.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
