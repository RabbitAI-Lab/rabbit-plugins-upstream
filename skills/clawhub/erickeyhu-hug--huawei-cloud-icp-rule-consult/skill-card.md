## Description: <br>
Provides read-only Huawei Cloud ICP filing rule consultation for filing requirements, processes, materials, account and entity limits, access filing, change filing, cancellation filing, APP filing, and migration scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Huawei Cloud after-sales technical engineers and support agents use this skill to answer customer ICP filing questions with concise, evidence-based guidance and relevant Huawei Cloud documentation links. It is limited to read-only consultation and does not perform filing operations. <br>

### Deployment Geography for Use: <br>
Global, for Mainland China ICP filing consultation on Huawei Cloud China-site documentation. <br>

## Known Risks and Mitigations: <br>
Risk: The web helpers can fetch or search live web content and may return changed or incomplete documentation. <br>
Mitigation: Prefer the embedded knowledge base and fixed Huawei Cloud documentation URLs, and present conclusions only when they are supported by retrieved or embedded evidence. <br>
Risk: Remote Chrome search can connect to an external browser endpoint. <br>
Mitigation: Use remote Chrome only when the endpoint is trusted; otherwise rely on embedded knowledge and the lightweight fetcher. <br>
Risk: ICP filing guidance can be misapplied outside the skill's stated scope. <br>
Mitigation: Keep answers limited to read-only Mainland China non-commercial ICP filing consultation and route domain registration, DNS, server purchase, real-name authentication, pricing, public security filing, and commercial filing elsewhere. <br>
Risk: Outdated dependencies may increase operational risk. <br>
Mitigation: Install current patched versions of the declared dependencies before using the optional web helpers. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-icp-rule-consult) <br>
- [Catalog routing reference](references/catalog.yml) <br>
- [Filing rules ontology](references/filing-rules.yml) <br>
- [Knowledge base](references/knowledge-base.md) <br>
- [Document command index](references/doc-commands.md) <br>
- [Prerequisites](references/prerequisites.md) <br>
- [Verification method](references/verification-method.md) <br>
- [Huawei Cloud ICP filing process](https://support.huaweicloud.com/usermanual-icp/zh-cn_topic_0000002127712329.html) <br>
- [Huawei Cloud regional filing requirements](https://support.huaweicloud.com/prepare-icp/icp_02_0005.html) <br>
- [Huawei Cloud access filing process](https://support.huaweicloud.com/usermanual-icp/zh-cn_topic_0000002581758204.html) <br>
- [Huawei Cloud APP feature information](https://support.huaweicloud.com/usermanual-icp/zh-cn_topic_0000002085120221.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text] <br>
**Output Format:** [Markdown or plain text with a direct answer, brief supporting details, and relevant document links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only consultation; prefers embedded knowledge and fixed Huawei Cloud documentation URLs before search; no filing operations are performed.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
