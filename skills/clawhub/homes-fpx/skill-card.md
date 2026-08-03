## Description: <br>
Query homes.com from a shell with the fpx CLI to search listings, resolve street addresses, fetch property details, photos, and history, and read the signed-in user's saved homes through their own browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to generate shell commands, extraction recipes, and guidance for retrieving Homes.com listing and saved-account data through an already signed-in browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use the user's signed-in Homes.com browser session, including saved homes and saved searches. <br>
Mitigation: Run saved-home or saved-search recipes only when account data access is intended, and avoid storing or sharing resulting HTML or parsed data unless explicitly desired. <br>
Risk: Homes.com responses can include sign-in redirects, WAF challenge pages, or close-but-not-confirmed address matches. <br>
Mitigation: Check for sign-in or WAF challenge responses and verify candidate property results against the requested address before relying on the output. <br>


## Reference(s): <br>
- [homes.com request recipes](artifact/references/homes-requests.md) <br>
- [ClawHub release page](https://clawhub.ai/chrischall/skills/homes-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell, JavaScript, and jq code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that fetch HTML or JSON through fpx and local parsing snippets for extracted listing data.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
