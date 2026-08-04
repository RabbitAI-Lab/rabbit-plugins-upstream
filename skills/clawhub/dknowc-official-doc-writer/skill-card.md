## Description: <br>
This skill helps agents draft, revise, review, and package Chinese official documents and formal organization materials using DKnowc outline/search services, local review guidance, and DOCX generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill to produce Chinese official documents, formal correspondence, policy-supported reports, DOCX deliverables, red-head document variants, and separate source-note HTML when search evidence is used. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Official-document outline and search workflows may send drafting details or sensitive policy topics to DKnowc external services. <br>
Mitigation: Use outline/search features only when the organization permits that third-party service use, and avoid submitting confidential drafting details unless approved. <br>
Risk: User-driven registration can save a local API key in the skill directory. <br>
Mitigation: Treat config.ini as a local secret, do not upload or package it, and rotate the API key if exposure is suspected. <br>
Risk: Generated official documents can include incorrect, unsupported, or misleading policy and data claims if source material is weak or unreviewed. <br>
Mitigation: Apply the bundled review checklist, verify high-risk claims against accepted sources, and keep searched source notes separate for human review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-official-doc-writer) <br>
- [Publisher profile](https://clawhub.ai/user/dylanzhangzx) <br>
- [DKnowc MaaS platform](https://platform.dknowc.cn/) <br>
- [DKnowc dependable search endpoint](https://open.dknowc.cn/dependable/search/) <br>
- [Search policy](reference/search_policy.md) <br>
- [Task router](reference/task_router.md) <br>
- [Output guide](reference/output_guide.md) <br>
- [Review checklist](reference/review_checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain-text drafts, DOCX files, HTML source-note files, JSON search or outline artifacts, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Long formal materials default to DOCX delivery; searched source material is separated into an HTML provenance note rather than embedded in the official document.] <br>

## Skill Version(s): <br>
3.2.5 (source: server evidence release.version, artifact _meta.json, README, and CHANGE_log.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
