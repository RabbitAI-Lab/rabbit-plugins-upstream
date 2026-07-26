## Description: <br>
Provides Python helpers and setup guidance for Tencent IMA knowledge-base operations, including OpenAPI note CRUD, cookie-authenticated knowledge-base management, RAG Q&A, folder operations, and subscribed knowledge bases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golngod](https://clawhub.ai/user/golngod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to connect to Tencent IMA, manage notes and knowledge bases, run knowledge-base Q&A, and configure authentication for IMA-backed workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles live IMA login cookies that can grant access to a user's knowledge-base data. <br>
Mitigation: Treat IMA_COOKIE like a password, avoid pasting it into shell history, do not commit ~/.hermes/.env, and rotate or delete the cookie if it is exposed. <br>
Risk: Authenticated test scripts can send live requests and may create notes or folders in an IMA account. <br>
Mitigation: Review scripts before execution and run them only on an account where those side effects are acceptable. <br>
Risk: Cookie authentication provides broader access than the scoped OpenAPI note workflow. <br>
Mitigation: Prefer scoped OpenAPI credentials for note-only workflows when the full cookie-authenticated feature set is not required. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/golngod/skills/ima-knowledge-base) <br>
- [Tencent IMA](https://ima.qq.com) <br>
- [Tencent IMA OpenAPI](https://ima.qq.com/openapi) <br>
- [IMA Knowledge Base Guide](README_KnowledgeBase.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python code and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce authenticated API call examples and local environment configuration guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
