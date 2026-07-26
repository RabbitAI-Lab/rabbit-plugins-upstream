## Description: <br>
Alibaba Bailian qwen3-tts voice cloning: upload a clean voice sample to create a custom voice for later text-to-speech use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to invoke the dLazy CLI for Alibaba Bailian qwen3-tts voice cloning from a clean audio sample. The resulting custom voice can be reused in later text-to-speech workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Voice samples may contain sensitive biometric data and are uploaded to a third-party cloud service. <br>
Mitigation: Use only recordings the user owns or has explicit permission to clone, and review dLazy retention and deletion terms before upload. <br>
Risk: The dLazy API key is stored in local CLI configuration when using the login or auth setup flow. <br>
Mitigation: Protect the local config file, prefer per-invocation environment variables when appropriate, and rotate or revoke organization keys from the dLazy dashboard if exposure is suspected. <br>
Risk: The examples include a stale prompt-style invocation that does not match the listed qwen-audio-clone options. <br>
Mitigation: Use `dlazy qwen-audio-clone -h` or tool description output as the source of truth before running the command. <br>
Risk: A persistent global CLI install increases local supply-chain and maintenance exposure. <br>
Mitigation: Prefer `npx @dlazy/cli@1.2.3` when a temporary pinned invocation is sufficient. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, JSON, guidance] <br>
**Output Format:** [CLI command guidance and JSON responses with generated output or task status URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and access to dLazy API and file-hosting endpoints.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
