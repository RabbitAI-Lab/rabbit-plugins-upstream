## Description: <br>
Generate standardized product requirements documents from customizable Jinja2 templates, with optional local Markdown output and Feishu document publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, developers, and product teams use this skill to draft consistent PRDs for general products, AI features, APIs, data products, and platform products. It supports both scripted and command-line workflows for generating Markdown and optionally preparing content for Feishu Docs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated PRDs may contain confidential roadmap, customer, API, architecture, prompt, or credential information. <br>
Mitigation: Review and redact sensitive content before saving generated documents or sharing them through Feishu. <br>
Risk: Optional Feishu publishing can send generated document content outside the local workspace. <br>
Mitigation: Use the Feishu path only for approved content and confirm the destination folder or wiki target before publishing. <br>
Risk: API-oriented templates may include insecure examples such as WebSocket tokens in URLs. <br>
Mitigation: Revise generated API authentication sections to keep tokens out of URLs and use approved secure authentication patterns. <br>


## Reference(s): <br>
- [Document Hub ClawHub listing](https://clawhub.ai/woai36d/skills/document-hub) <br>
- [Document Hub skill documentation](artifact/SKILL.md) <br>
- [PRD generation workflow](artifact/scripts/generate_prd.py) <br>
- [Template rendering engine](artifact/scripts/template_engine.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown documents, Python snippets, command-line examples, and JSON-like generation results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write generated PRDs to local files and can prepare content for optional Feishu document creation when that integration is available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
