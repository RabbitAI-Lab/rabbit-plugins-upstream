## Description:

筑龙标事通标书智能写作 helps an agent interpret tender documents, generate bid documents, and review bid compliance through the 百炼®标书 cloud service after the user provides local tender or bid files and an App Key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and procurement support users use this skill to analyze tender requirements, draft editable bid documents, and produce compliance review reports for supplied tender and bid files. It is intended for file-backed bid workflows where the user understands that documents are processed by the stated cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm the user is comfortable uploading the selected files before use and rely only on user-provided local files.

Risk: The App Key is tied to the user's account balance and grants access to the service.

Mitigation: Keep the App Key out of chat, store it only in the local config.json file as directed, and use logout or delete config.json when the credential should no longer be retained.

Risk: A custom service base setting changes where files and requests are sent.

Mitigation: Review any custom ZCM_BASE or stored base setting before use and keep the default stated service endpoint unless the user intentionally configured another trusted endpoint.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-guard)
- [Usage Guide](references/usage.md)
- [API Reference](references/api.md)
- [百炼®标书 Website](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, JSON API results, HTML or Word reports, and editable .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on user-supplied local tender or bid files and an App Key tied to the user's account balance.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
