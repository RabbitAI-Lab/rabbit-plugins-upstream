## Description: <br>
Provides LinkFox gateway helpers and reference material for Temu US product-management APIs covering product lookup, edits, deletion, inventory, listing status, pre-sale settings, category checks, attributes, compliance, external IDs, and video cover retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
E-commerce operators and developers use this skill to query and update Temu US product catalog data through LinkFox-mediated Temu Partner APIs. It is suited for controlled product-management workflows such as stock changes, listing status changes, compliance edits, and product deletion after human review. <br>

### Deployment Geography for Use: <br>
United States Temu marketplace operations; user deployment is not otherwise restricted by the provided evidence. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles reusable LinkFox and Temu merchant tokens. <br>
Mitigation: Treat tokens as secrets, prefer environment variables or store keys over pasting raw tokens into chat, and remove local token files when access is no longer needed. <br>
Risk: The skill can perform live product-management actions such as update, delete, stock, status, and compliance changes. <br>
Mitigation: Review generated commands and payloads before execution, especially for delete and update operations, and verify target product IDs and store context. <br>
Risk: Full API responses are saved locally and may include sensitive catalog or account data. <br>
Mitigation: Limit inline output for large or sensitive responses and clear local response files after completing the workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-manage-product-us) <br>
- [API reference](artifact/references/api.md) <br>
- [Partner US Manage Product catalog](artifact/references/partner-us-catalog.md) <br>
- [Per-interface API index](artifact/references/apis/README.md) <br>
- [Temu Partner US Manage Product documentation](https://partner-us.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=2a343c65a03d42d380e9ad835aa7b54b) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON files] <br>
**Output Format:** [Markdown guidance with Python command examples and JSON API responses written to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts save full responses under a local linkfox session directory and print either full JSON or a summary depending on response size and inline mode.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
