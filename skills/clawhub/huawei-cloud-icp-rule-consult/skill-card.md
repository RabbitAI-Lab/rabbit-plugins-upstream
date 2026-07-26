## Description: <br>
Provides read-only consultation on Huawei Cloud mainland China ICP filing requirements, processes, materials, and filing-change scenarios using embedded guidance and optional official-document lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Huawei Cloud after-sales technical engineers use this skill to answer customer questions about non-commercial mainland China ICP filings, including whether filing is needed, required materials, access filing, change filing, cancellation filing, APP filing, migration, and account or entity limits. <br>

### Deployment Geography for Use: <br>
Mainland China <br>

## Known Risks and Mitigations: <br>
Risk: The bundled web tools can fetch or browse arbitrary sites even though the intended purpose is Huawei Cloud ICP documentation consultation. <br>
Mitigation: Restrict network access to Huawei Cloud ICP documentation domains, block localhost and private-network targets, and avoid untrusted remote Chrome endpoints. <br>
Risk: Users may rely on filing guidance in sensitive compliance workflows. <br>
Mitigation: Review answers against the cited Huawei Cloud ICP documentation before using them for filing decisions. <br>


## Reference(s): <br>
- [Huawei Cloud ICP filing process](https://support.huaweicloud.com/usermanual-icp/zh-cn_topic_0000002127712329.html) <br>
- [Huawei Cloud access filing process](https://support.huaweicloud.com/usermanual-icp/zh-cn_topic_0000002581758204.html) <br>
- [Huawei Cloud regional filing requirements](https://support.huaweicloud.com/prepare-icp/icp_02_0005.html) <br>
- [Huawei Cloud APP filing characteristic information](https://support.huaweicloud.com/usermanual-icp/zh-cn_topic_0000002085120221.html) <br>
- [Embedded ICP filing knowledge base](references/knowledge-base.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text customer-facing answers with relevant document links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only consultation; embedded knowledge is preferred before document fetch or search; web_search is limited to one call and combined web_fetch/web_search calls are limited to three.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
