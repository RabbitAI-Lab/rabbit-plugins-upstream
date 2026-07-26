## Description: <br>
Detects PC hardware config via PowerShell, estimates second-hand price for Xianyu (闲鱼), generates valuation report, product poster, and listing copy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to inventory a Windows PC, estimate its second-hand resale value, and generate Xianyu sale materials such as an HTML valuation report, a product poster, and listing copy. It is intended for people preparing to sell their own computer hardware. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill inventories local hardware and attached devices, which can reveal device details in generated reports or listings. <br>
Mitigation: Run it only on a computer you are authorized to sell and review generated materials before publishing. <br>
Risk: Generated sale materials may include storage or device details that the seller does not want to disclose publicly. <br>
Mitigation: Remove sensitive device identifiers from the listing and wipe personal data before transferring the machine. <br>
Risk: Second-hand market prices can fluctuate and generated valuations may be inaccurate. <br>
Mitigation: Compare the estimate against current marketplace listings before setting the final sale price. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/skills/pc-secondhand) <br>
- [二手电脑配件估价参考（2025-2026市场行情）](artifact/references/price-guide.md) <br>
- [咸鱼出售文案模板](artifact/references/listing-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [PowerShell command snippets, HTML files, Markdown or plain-text listing copy, and concise sale strategy guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate or embed a product image when image generation is available; otherwise advises using real product photos.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
