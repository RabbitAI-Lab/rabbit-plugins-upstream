## Description: <br>
Tencent Cloud COS helps agents manage Tencent Cloud object storage, Data Intelligence processing, MetaInsight retrieval, and knowledge-base workflows through guided setup and Node.js command execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shawnminh](https://clawhub.ai/user/shawnminh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure Tencent Cloud COS credentials, run storage and CI processing commands, create knowledge bases, and retrieve or process cloud-hosted content. It is intended for workflows where Tencent Cloud COS access is explicitly desired. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact Tencent Cloud storage and CI operations using sensitive cloud credentials. <br>
Mitigation: Install it only for explicit Tencent Cloud COS workflows and use least-privilege sub-account keys or short-lived STS credentials. <br>
Risk: Credential handling can expose permanent cloud keys if users choose plaintext persistence. <br>
Mitigation: Prefer ephemeral environment variables or STS tokens, avoid plaintext .env persistence, and never echo SecretId or SecretKey in chat. <br>
Risk: Delete operations and generic CI requests may change or remove cloud resources or trigger unexpected costs. <br>
Mitigation: Review delete, batch delete, bucket policy, and ci-request actions before execution, and confirm Tencent Cloud fees before running processing jobs. <br>


## Reference(s): <br>
- [Tencent Cloud COS Skill Page](https://clawhub.ai/shawnminh/skills/tencentcloud-cos) <br>
- [COS Node.js SDK Operation Reference](artifact/references/api_reference.md) <br>
- [Tencent Cloud COS Node.js SDK](https://cloud.tencent.com/document/product/436/8629) <br>
- [Tencent Cloud Data Intelligence](https://cloud.tencent.com/document/product/460) <br>
- [Tencent Cloud COS Fees](https://cloud.tencent.com/document/product/436/16871) <br>
- [Tencent Cloud CI Fees](https://cloud.tencent.com/document/product/460/6970) <br>
- [cos-nodejs-sdk-v5 GitHub](https://github.com/tencentyun/cos-nodejs-sdk-v5) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Tencent Cloud COS region and bucket configuration plus SecretId/SecretKey or an STS token.] <br>

## Skill Version(s): <br>
1.1.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
