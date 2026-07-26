## Description: <br>
Download product images from any public Shopify store without API access, including full backups, collection-only exports, single-product downloads, optional WebP conversion, and smart renaming. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to preview and download public Shopify product images for backup, collection export, single-product export, filename cleanup, or optional WebP conversion. The workflow is read-only against the store and writes downloaded assets to a user-selected local directory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional WebP conversion can run npm to install sharp and create dependency files in the skill script directory. <br>
Mitigation: Use the downloader without WebP conversion, or manually install and review sharp before enabling WebP. <br>
Risk: The skill downloads files from public Shopify storefronts into a local output directory. <br>
Mitigation: Preview counts first, keep overwrite disabled unless explicitly needed, and choose an output directory intended for downloaded store assets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lvsao/skills/shopify-product-images-downloader) <br>
- [Project homepage from package metadata](https://github.com/lvsao/shopify-skill-hub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance, files] <br>
**Output Format:** [Markdown-style agent guidance with shell command examples, downloaded image files, and a plain-text download summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js; downloads public Shopify image assets into a user-selected output directory and can optionally rename files or convert images to WebP.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
