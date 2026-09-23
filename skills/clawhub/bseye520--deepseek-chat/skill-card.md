## Description:

Provides a Node.js command-line chat client for sending prompts to the DeepSeek API and printing model responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bseye520](https://clawhub.ai/user/bseye520)

### License/Terms of Use:


## Use Case:

Developers and external users can use this skill to run DeepSeek chat prompts from an agent-accessible command line and receive response text with token usage. Users should review the security guidance before installing or sending private prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes an apparent plaintext DeepSeek API key.

Mitigation: Treat the bundled key as exposed, remove or replace it, and supply a user-owned secret securely at runtime.

Risk: Prompts and any included content are transmitted to a third-party DeepSeek API.

Mitigation: Do not send secrets, proprietary files, regulated data, or private prompts unless that transfer is acceptable for the deployment.

Risk: The skill text claims file processing and online search support, while the artifact behavior only shows a chat CLI.

Mitigation: Clarify or remove unsupported feature claims before relying on those capabilities.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bseye520/skills/deepseek-chat)
- [DeepSeek platform](https://platform.deepseek.com)
- [DeepSeek API endpoint](https://api.deepseek.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration]

**Output Format:** [Plain text command-line output with model response text and token usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a DeepSeek API key supplied through DEEPSEEK_API_KEY.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
