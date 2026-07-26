## Description: <br>
Identifies insects or other arthropods from an image URL or Base64 image data, including likely order, family, genus, or species. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit an insect or arthropod image and receive identification results from the Xiaobenyang API. It is useful for field, educational, or cataloging workflows where the user can provide a valid API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends insect images or image URLs to an external API. <br>
Mitigation: Use it only with images the user is permitted to share and disclose the external API dependency before use. <br>
Risk: The skill stores XBY_APIKEY in a local plaintext .env file. <br>
Mitigation: Use a dedicated, scoped API key, avoid sensitive or reused credentials, and rotate the key if it may have been exposed. <br>
Risk: The security summary reports mismatched gaokao or school-service references in the package. <br>
Mitigation: Review the skill behavior before installation and treat the output as unverified until the publisher resolves the mismatched references. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/insect-recognition) <br>
- [ALinkLab publisher profile](https://clawhub.ai/user/alinklab) <br>
- [Xiaobenyang service site](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API calls, Guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided XBY_APIKEY and either an image URL or Base64-encoded image data.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
