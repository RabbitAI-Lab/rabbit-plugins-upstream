## Description: <br>
Fetches customer reviews for Taobao or Tmall product pages by item ID, including reviewer name, date, purchased variant, review text, photo URLs, and pagination support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to collect Taobao or Tmall product review data from pages visible in their logged-in browser session for review analysis, dataset building, or rating-change monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation runs in a logged-in Taobao session and can access product review pages visible to the user. <br>
Mitigation: Install only when comfortable with browser automation in that session, and use a session scoped to the intended Taobao or Tmall product pages. <br>
Risk: Operational notes may be retained locally if unexpected page behavior is encountered. <br>
Mitigation: Review or remove the configured local memory file if retaining operational notes is not desired. <br>
Risk: Extracted reviews and photo URLs may include user-generated content. <br>
Mitigation: Handle exported review data according to applicable privacy, platform, and content-use requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/taobao-product-reviews) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/browseract-cli) <br>
- [Taobao product page URL format](https://item.taobao.com/item.htm?id={itemId}) <br>
- [Taobao login and site entry](https://www.taobao.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON review records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Review records include username, date, purchasedSku, content, photos, and rating when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
