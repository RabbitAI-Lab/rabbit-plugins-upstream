## Description: <br>
本地离线OCR识别图片/PDF发票，自动分类专票/普票/电子普票，生成月度报销台账，断网可用，财务数据不向外传输。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincent-chao-lang](https://clawhub.ai/user/vincent-chao-lang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Small business finance and tax users use this skill to process a user-selected folder of invoice PDFs or images locally, extract invoice fields, classify invoice types, validate totals, and generate a monthly reimbursement ledger with an exception sheet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Invoice images may be sent to the configured OLLAMA_API endpoint during VLM fallback, and the artifact does not enforce that this endpoint is local. <br>
Mitigation: Keep OLLAMA_API pointed at a trusted local Ollama service, preferably localhost, and review the setting before processing sensitive invoices. <br>
Risk: Unpinned Python dependencies process sensitive invoice files. <br>
Mitigation: Review, pin, and update dependencies in a controlled environment before using the skill on sensitive or third-party invoices. <br>
Risk: OCR or VLM-assisted extraction can leave invoice fields incomplete or inconsistent. <br>
Mitigation: Review the generated exception sheet and risk remarks before using the ledger for reimbursement, tax, or accounting decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincent-chao-lang/skills/tax-invoice-skill) <br>
- [Publisher profile](https://clawhub.ai/user/vincent-chao-lang) <br>
- [Ollama local model runtime](https://ollama.com) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Excel workbook (.xlsx) with terminal status text and setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates a monthly ledger sheet and an exception sheet for invoices that need review.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
