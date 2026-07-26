## Description: <br>
Private local document AI for Intel hardware. Parse PDFs, invoices, screenshots, and diagrams with MinerU 2.5 on OpenVINO GenAI, keep the model warm in a local service, and output structured JSON/Markdown with user-defined invoice fields. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhuo-yoyowz](https://clawhub.ai/user/zhuo-yoyowz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and business users use this skill to process local PDFs, invoices, screenshots, and diagrams into private structured records, Markdown parse outputs, reports, and draft code or notebook artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can start a local background document service. <br>
Mitigation: Keep the service bound to 127.0.0.1 and do not expose it to external networks. <br>
Risk: Parsed documents and generated reports may be stored as plaintext artifacts. <br>
Mitigation: Use a private output directory for sensitive documents and delete artifacts after review. <br>
Risk: Generated notebooks or code drafts may include remote model-loading behavior. <br>
Mitigation: Review generated notebooks before execution and remove or approve remote model-loading code such as trust_remote_code=True. <br>
Risk: Runtime dependencies and local model bundles affect the trust boundary. <br>
Mitigation: Pin or audit dependencies and install model assets only from sources approved for the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhuo-yoyowz/skills/local-document-ai-openvino) <br>
- [Mode Guide](references/mode_guide.md) <br>
- [Output Contracts](references/output_contracts.md) <br>
- [Schema](references/schema.md) <br>
- [MinerU 2.5 Pro OpenVINO INT4 model bundle](https://www.modelscope.cn/models/snake7gun/MinerU2.5-Pro-2604-1.2B-int4-ov) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [JSON, Markdown, HTML reports, code or notebook drafts, and shell command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written to local artifact folders with traceability files when available.] <br>

## Skill Version(s): <br>
0.4.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
